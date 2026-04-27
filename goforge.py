# /GoForge/goforge.py
# Launcher for GoForge
# Created By: David Kistner (Unconditional Love) at GlyphicMind Solutions LLC.



# system imports
import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication

# local imports
from engine.llm_engine import LLMEngine
from gui.goforge_window import GoForgeWindow



# -----------------
# Main Entry Point
# -----------------
def main():
    base_dir = Path(__file__).parent.resolve()

    manifest_path = base_dir / "models" / "manifest.yaml"
    storage_root = base_dir / "storage"

    # Ensure storage directories exist
    (storage_root / "logs").mkdir(parents=True, exist_ok=True)
    (storage_root / "pending").mkdir(parents=True, exist_ok=True)
    (storage_root / "saved").mkdir(parents=True, exist_ok=True)

    # Load LLM engine
    llm = LLMEngine(manifest_path)

    # Launch GUI
    app = QApplication(sys.argv)
    window = GoForgeWindow(llm, storage_root)
    window.show()

    sys.exit(app.exec_())


# --------------------------
# Standard Python Entrypoint
# --------------------------
if __name__ == "__main__":
    main()

