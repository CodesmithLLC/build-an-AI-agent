import requests, json, sys, pathlib
from datetime import datetime, timedelta, timezone

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
LOG_FILE = SCRIPT_DIR / "screenshot_agent.log"
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbyvMNYEaLwVSts0CN-mc4rx0jxz92gIIqcWO_XGU8Tsj5e2PtVRn__ezHxBQNqNBw64/exec"

def log(msg: str):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now().strftime('%-I:%M:%S %p')} - {msg}\n")

def _json_only(s: str) -> dict:
    s = s.strip()
    # If the model wrapped JSON in code fences or added prose, try to locate the first/last braces
    start = s.find("{")
    end = s.rfind("}")
    if start != -1 and end != -1 and end > start:
        s = s[start:end+1]
    return json.loads(s)


parsed_json = _json_only(sys.argv[1])
payload = parsed_json

r = requests.post(WEB_APP_URL, headers={"Content-Type": "application/json"}, data=json.dumps(payload))

log(f"Event posted {r.text}")