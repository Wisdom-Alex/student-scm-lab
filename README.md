# Student Score Manager

A small modular Python project used for SEN 401 (Software Configuration Management and Maintenance).
Requires **Python 3.9 or newer** (tested on 3.9 and 3.12).

## Project structure

| Path | Purpose |
|------|---------|
| `app.py` | Main script that runs the demo application |
| `students.py` | Data module: Pydantic `Student` model and the student list |
| `utils/helpers.py` | Statistics: highest, lowest, average, median, letter grade |
| `utils/report.py` | Console report formatting |
| `tests/test_students.py` | Unit tests (standard library `unittest`) |
| `requirements.txt` | Dependency list (Pydantic) |

## Setup and usage

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
python -m unittest -v
```

## Releases

| Tag | Description |
|-----|-------------|
| v1.0 | Baseline starter code |
| v1.1 | Corrective, adaptive, perfective and preventive maintenance |
