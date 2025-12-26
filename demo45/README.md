# Gemini RAG Chatbot

Quick start

1. Install dependencies:

```powershell
pip install -r requirements.txt
```

2. Set your Gemini API key (one of these):

- For the current PowerShell session:

```powershell
$env:GEMINI_API_KEY = "YOUR_API_KEY"
python .\app.py
```

- Or create a `.env` file in the project root with:

```
GEMINI_API_KEY=YOUR_API_KEY
```

Then run:

```powershell
python .\app.py
```

Notes: If you use `setx` on Windows, open a new terminal for it to take effect.
