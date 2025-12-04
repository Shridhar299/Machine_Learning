## HealthRiskPrediction Web App

A small Flask-based web application for local healthcare risk predictions.

### Prerequisites

- Python 3.8 or newer
- pip (comes with Python)

### Quick start (Windows PowerShell)

1. Create a virtual environment (use the Python launcher for 3.8):

```powershell
py -3.8 -m venv venv
```

2. Activate the virtual environment (PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

If you use Command Prompt (cmd.exe) instead of PowerShell:

```cmd
.\venv\Scripts\activate.bat
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Run the Flask app:

```powershell
python app.py
```

By default the development server runs on http://127.0.0.1:5000/ (or http://localhost:5000/).

### Notes & Troubleshooting

- If you see "Address already in use", stop the running process or change the port in `app.py`.
- If packages are missing, double-check that your virtual environment is active and re-run
	`pip install -r requirements.txt`.
- For macOS/Linux, replace PowerShell activation commands with:

```bash
source venv/bin/activate
```

### Project structure (top-level)

- `app.py` — Flask app launcher
- `website/` — application package (views, templates, static files)
- `requirements.txt` — Python dependencies

### Contact / Next steps

If you want, I can:

- Add a development Makefile or PowerShell script to automate setup
- Pin exact dependency versions in `requirements.txt` or add a `pyproject.toml`
- Add a short CONTRIBUTING or NOTE about how to run tests (if tests are added)

---

Enjoy exploring the app! 🚀