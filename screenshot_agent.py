import subprocess, pathlib, sys, datetime

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
LOG_FILE = SCRIPT_DIR / "screenshot_agent.log"

time_str = datetime.datetime.now().strftime('%-I:%M:%S %p')
file_path = sys.argv[1] if len(sys.argv) > 1 else None

def log(msg: str):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now().strftime('%-I:%M:%S %p')} - {msg}\n")

log(f"Got: {file_path}")

# Run the next stage (extract_event.py) in a new subprocess
subprocess.run([sys.executable, str(SCRIPT_DIR / "extract_event.py"), file_path or ""])
