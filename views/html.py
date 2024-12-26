from pathlib import Path

BASE_ROOT = Path(__file__).resolve().parent
with open(f"{BASE_ROOT}/index.html", "r", encoding="utf8") as file:
    html_index = file.read()