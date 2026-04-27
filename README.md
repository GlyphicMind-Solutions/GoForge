# ⭐ GoForge — Go Code Forge
- Created By: David Kistner (Unconditional Love)  
- GlyphicMind Solutions LLC

- GoForge is a local‑first Go code generation and refactoring tool built on the GlyphicMind Forge architecture.
- It provides a full IDE‑style workflow powered by local .gguf models via llama_cpp_python, including:
   1. Model‑family‑aware prompt building
   2. Multi‑file Go module generation using // FILE: markers
   3. Go module‑aware path handling (main.go, pkgname/file.go, cmd/app/main.go)
   4. Deep Analysis v2 (chunk → summarize → meta‑summarize → reconstruct)
   5. Tabbed GUI with staging, master code, and logs
   6. Brand‑tagged file forging into storage/pending
   7. Full local control — no cloud dependencies

GoForge is part of the GlyphicMind Solutions Forge Suite, alongside PythonForge, JavaScriptForge, CSharpForge, CppForge, JavaForge, and RustForge.

---

## 🚀 Features
### 🔥 Local‑First LLM Execution
JavaForge loads `.gguf` models defined in:
```
models/manifest.yaml

```

Supports:
- GPT‑OSS  
- Mistral  
- Llama  
- Qwen  
- DeepSeek  
- Phi  
- Any LocalAI‑compatible `.gguf` model  

---

### 🧠 Deep Analysis v2
JavaForge includes the upgraded Deep Analysis engine:

- Splits large codebases into chunks  
- Summarizes each chunk  
- Produces a meta‑summary  
- Reconstructs/refactors the entire project  
- Logs every step in the Deep Analysis Log tab  

---

### 🧩 Multi‑File Go Module Output
GoForge automatically detects and writes multiple files when the model outputs:
```
// FILE: main.go
// FILE: pkgname/service.go
// FILE: cmd/app/main.go

```

---

### 📦 Go Module‑Aware Path Support
If the model outputs module‑structured paths, GoForge writes files exactly where they belong:
```
storage/pending/main.go
storage/pending/pkg/service.go
storage/pending/cmd/app/main.go
```

---

### 🖥️ Full GUI (PyQt5)

- Tabbed IDE layout:
   1. Topic / Corrections
   2. Raw LLM Output
   3. Extracted Code
   4. Master Code
   5. Deep Analysis Log

- Global controls:
   1. Generate
   2. Re‑run with Corrections
   3. Deep Analysis
   4. Open File
   5. Save File
   6. Forge → Pending
   7. Clear Session

---

### 🗂️ Storage System

JavaForge organizes output into:

```
storage/
    pending/   ← forged files awaiting review
    saved/     ← user‑saved files
    logs/      ← forge.log + deep analysis logs
```

---

## ⭐ Installation

1. Create a virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Add your .gguf models
Place them in:
```
models/
```
Then update:
```
models/manifest.yaml
```

---

## ⭐ Running GoForge

In your terminal, or Command Prompt type in your directory:
```
python3 goforge.py
```

---

### ⭐ Model Manifest Example
```
models:
  mistral_default:
    path: ./models/mistral-7b-instruct-v0.2.Q4_K_M.gguf <--- you can change this to the directory of your model
    n_ctx: 32768
    template: mistral
```

---

# ⭐ Part of the GlyphicMind Forge Suite

JavaForge is one of many Forge tools:

1. ✅️ PythonForge

2. ✅️ JavaScriptForge

3. ✅️ CSharpForge

4. ✅️ CppForge

5. ✅️ JavaForge

6. ✅️ RustForge

7. ✅️ GoForge (coming)

8. HTML/CSS Forge

9. SQLForge

--All tools follow the same architecture, branding, and workflow.

---

### ⭐License

This project is part of the GlyphicMind Solutions ecosystem.
All rights reserved.
