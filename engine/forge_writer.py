# /GoForge/engine/forge_writer.py
# GoForge File Writer (multi-file module support)
# Created By: David Kistner (Unconditional Love) at GlyphicMind Solutions LLC.



# system imports
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List



# ===========================================
# FORGE WRITER CLASS
# ===========================================
class ForgeWriter:
    """
    ForgeWriter
    - Writes Go files into storage/pending or storage/saved
    - Supports multi-file output using // FILE: markers
    - Supports Go module-style paths:
        - main.go
        - pkgname/file.go
        - cmd/app/main.go
    - Injects brand tag
    - Logs all actions
    """

    # --------------
    # Initialize
    # --------------
    def __init__(self, storage_root: Path):
        self.storage_root = Path(storage_root)
        self.pending_dir = self.storage_root / "pending"
        self.saved_dir = self.storage_root / "saved"
        self.logs_dir = self.storage_root / "logs"
        self.log_path = self.logs_dir / "forge.log"

        self.pending_dir.mkdir(parents=True, exist_ok=True)
        self.saved_dir.mkdir(parents=True, exist_ok=True)
        self.logs_dir.mkdir(parents=True, exist_ok=True)

    # -------------------------
    # Inject Brand Tag
    # -------------------------
    def _inject_brand_tag(self, code: str) -> str:
        """
        Injects GlyphicMind Solutions Brand into Go file.
        """
        lines = code.splitlines()
        brand = "//--- Created with GlyphicMind Solutions: GoForge ---//"

        if len(lines) >= 3:
            lines.insert(2, brand)
        else:
            while len(lines) < 2:
                lines.append("")
            lines.append(brand)

        return "\n".join(lines)

    # -------------------------
    # Detect multi-file output
    # -------------------------
    def _split_go_files(self, raw: str) -> Dict[str, str]:
        """
        Detects and splits multi-file Go output.

        Expected patterns:
            // FILE: main.go
            // FILE: pkgname/file.go
            // FILE: cmd/app/main.go
        """
        files: Dict[str, str] = {}
        current_name = None
        current_lines: List[str] = []

        for line in raw.splitlines():
            if line.strip().startswith("// FILE:"):
                # save previous file
                if current_name and current_lines:
                    files[current_name] = "\n".join(current_lines).strip()

                # start new file
                current_name = line.split(":", 1)[1].strip()
                current_lines = []
            else:
                if current_name:
                    current_lines.append(line)

        # save last file
        if current_name and current_lines:
            files[current_name] = "\n".join(current_lines).strip()

        return files

    # -------------------------
    # Infer filename for single-file output
    # -------------------------
    def _infer_filename(self, topic: str) -> str:
        """
        If the user doesn't specify a file, default to main.go.
        """
        t = topic.lower()

        if "cmd/" in t or "command" in t:
            return "cmd/app/main.go"

        return "main.go"

    # -------------------------
    # Forge script(s)
    # -------------------------
    def forge_script(self, filename: str, code: str, purpose: str = "") -> bool:
        """
        Forges Go file(s) and writes them to storage/pending.
        Supports multi-file output and module-style paths.
        """
        # Detect multi-file output
        file_map = self._split_go_files(code)

        # Single-file mode
        if not file_map:
            if not filename.endswith(".go"):
                filename = self._infer_filename(filename)

            target_path = self.pending_dir / filename
            target_path.parent.mkdir(parents=True, exist_ok=True)

            code = self._inject_brand_tag(code)

            try:
                target_path.write_text(code, encoding="utf-8")
            except Exception as e:
                print(f"⚠️ Failed to write Go file: {e}")
                return False

            self._log_event("forge_pending", {
                "filename": filename,
                "purpose": purpose,
                "path": str(target_path)
            })

            print(f"🛠️ Go file forged (pending): {target_path}")
            return True

        # Multi-file mode
        success = True
        for fname, fcode in file_map.items():
            fcode = self._inject_brand_tag(fcode)

            target_path = self.pending_dir / fname
            target_path.parent.mkdir(parents=True, exist_ok=True)

            try:
                target_path.write_text(fcode, encoding="utf-8")
            except Exception as e:
                print(f"⚠️ Failed to write Go file '{fname}': {e}")
                success = False
                continue

            self._log_event("forge_pending", {
                "filename": fname,
                "purpose": purpose,
                "path": str(target_path)
            })

            print(f"🛠️ Go file forged (pending): {target_path}")

        return success

    # -------------------------
    # Save script(s)
    # -------------------------
    def save_script(self, filename: str, code: str) -> bool:
        """
        Saves Go file(s) directly to storage/saved.
        Supports multi-file output and module-style paths.
        """
        file_map = self._split_go_files(code)

        # Single file
        if not file_map:
            if not filename.endswith(".go"):
                filename = self._infer_filename(filename)

            target_path = self.saved_dir / filename
            target_path.parent.mkdir(parents=True, exist_ok=True)

            code = self._inject_brand_tag(code)

            try:
                target_path.write_text(code, encoding="utf-8")
            except Exception as e:
                print(f"⚠️ Failed to save Go file: {e}")
                return False

            self._log_event("save_script", {
                "filename": filename,
                "path": str(target_path)
            })

            print(f"💾 Go file saved: {target_path}")
            return True

        # Multi-file
        success = True
        for fname, fcode in file_map.items():
            fcode = self._inject_brand_tag(fcode)

            target_path = self.saved_dir / fname
            target_path.parent.mkdir(parents=True, exist_ok=True)

            try:
                target_path.write_text(fcode, encoding="utf-8")
            except Exception as e:
                print(f"⚠️ Failed to save Go file '{fname}': {e}")
                success = False
                continue

            self._log_event("save_script", {
                "filename": fname,
                "path": str(target_path)
            })

            print(f"💾 Go file saved: {target_path}")

        return success

    # -------------------------
    # Log event
    # -------------------------
    def _log_event(self, event_type: str, details: dict):
        """
        Logs the event to storage/logs/forge.log
        """
        entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "event_type": event_type,
            "details": details,
        }

        try:
            with open(self.log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry) + "\n")
        except Exception as e:
            print(f"⚠️ Failed to write forge log: {e}")

