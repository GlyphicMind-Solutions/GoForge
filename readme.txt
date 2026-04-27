⭐ GoForge User Guide
Created by: David Kistner (Unconditional Love) at GlyphicMind Solutions LLC.

What is GoForge?
GoForge is a Go code creation and refactoring tool powered by local LLMs.
You describe what you want in plain English, and GoForge generates Go modules, packages, and files automatically.
It supports:
-Single‑file Go programs
-Multi‑file Go modules using // FILE: markers
-Package structures (pkg/, cmd/app/, etc.)
-Deep Analysis (summaries → meta‑summary → reconstructed code)
-A full GUI workflow with staging and master code areas
-Everything runs locally — no cloud, no API keys.
-Before You Start
-You must assign your model path in:
/GoForge/models/manifest.yaml
Example manifest.yaml models:
  gpt_oss_20b:
    path: ./models/gpt-oss-20b.Q4_K_M.gguf <---- you can edit the path to your own LLM location, or just drop the LLM in the models folder
    n_ctx: 32768
    template: gpt

Once your model is set, GoForge is ready.


How to Use GoForge
1. Enter a Forge Topic
In the Topic / Corrections tab, write what you want GoForge to create.
Example:
in the forge topic box type-
"Create a simple Go module with a Greeter struct and a Greet() method."
-Then click Generate.

2. Wait for Raw LLM Output
The model will produce Go code in the Raw LLM Output tab.
If the model outputs multiple files, it will use:

Code
 // FILE: main.go
 // FILE: pkg/helpers.go

GoForge automatically detects and splits these.

3. Review Extracted Code
GoForge extracts the actual Go code into the Extracted Code tab.
You can edit this code before moving it into Master Code.

4. Use Corrections (Optional)
If you want changes:
-Write your instructions in the Corrections box
-Click Re‑run with Corrections
-GoForge will refine the code based on your feedback.

5. Move Final Code to Master Code
When you’re satisfied with the extracted code:
-Copy it into the Master Code tab
-This is your final working area
-Saving and forging both use this tab

6. Save or Forge the Code
You have two options:
-Save File
Saves the code directly to a .go file of your choosing.
-Forge → Pending
Writes the code into:
Code
/GoForge/storage/pending/
This is useful for multi‑file modules or when you want to review before integrating into a larger system.

Deep Analysis (Optional but Powerful)
Deep Analysis reads your Go code and:
-Splits it into chunks
-Summarizes each chunk
-Merges all summaries into a meta‑summary
-Reconstructs/refactors the entire module
-Outputs improved Go code

The Deep Analysis Log tab shows every step.
This is ideal for:
-messy code
-large files
-refactoring
-improving structure
-converting multi‑file modules



*Important Notes
--Brand Tag
GoForge adds a small brand signature to the top of each file.
You may remove it if you prefer — just ensure it doesn’t break your code.
--Blank Lines
If you want to avoid the signature interfering with your code, leave 5 blank lines at the top before saving.




Multi‑File Output
If the model uses // FILE: markers, GoForge will:
-split the files
-create directories automatically
-write them into storage/pending or storage/saved

Example Forge Topic
Code
Create a Go module with two files:
main.go should call a Sum() function.
utils/helpers.go should define Sum(a, b int) int.
Use idiomatic Go imports.
Output using // FILE: markers.
End with FIN~.
That’s it — GoForge is ready to use
