# extract_event.py
import sys, pathlib, base64, requests, json, traceback, subprocess, time
from datetime import datetime, timedelta, timezone
from pathlib import Path

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
LOG_FILE = SCRIPT_DIR / "screenshot_agent.log"

OPENAI_API_KEY = "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"   # <-- your key

def log(msg: str):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now().strftime('%-I:%M:%S %p')} - {msg}\n")

def describe_image(file_path: Path) -> str:
    b64 = base64.b64encode(file_path.read_bytes()).decode("utf-8")
    ext = file_path.suffix.lower()
    mime = "image/png" if ext == ".png" else ("image/jpeg" if ext in (".jpg",".jpeg") else "image/png")

    payload = {
        "model": "gpt-5-mini",
        "input": [{
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": (
                        extract_prompt
                    )
                },
                {
                    "type": "input_image",
                    "image_url": f"data:{mime};base64,{b64}"
                }
            ]
        }]
    }
    log(f"Sending to OpenAI {payload['model']}")
    import traceback
    import json
    import requests

    try:
        r = requests.post(
            "https://api.openai.com/v1/responses",
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=90,  # images can be slow; 30s is often too tight
        )
        r.raise_for_status()
        data = r.json()

        # Fast path: consolidated helpers first
        if data.get("output_text"):
            return "".join(data["output_text"]).strip()

        # Fallback: walk the structured output array
        for part in (data.get("output") or []):
            for chunk in part.get("content", []):
                if chunk.get("type") in ("output_text", "summary_text"):
                    return (chunk.get("text") or "").strip()

        # Last resort: return the whole JSON as a string (useful for debugging)
        return json.dumps(data)

    except requests.Timeout as e:
        log(f"Timeout error: {e}")
        log(f"Payload size (bytes): {len(json.dumps(payload))}")
        log(f"Stack trace:\n{traceback.format_exc()}")
        return ""

def main():
    try:
        fp = Path(sys.argv[1])
        if not fp.exists():
            log(f"file not found: {fp}")
            print(f"ERROR: file not found: {fp}")
            sys.exit(2)
        if not OPENAI_API_KEY or OPENAI_API_KEY.startswith("sk-REPLACE"):
            log("OPENAI_API_KEY missing/placeholder")
            print("ERROR: OPENAI_API_KEY missing/placeholder")
            sys.exit(1)
        desc = describe_image(fp)
        log(f"Image described successfully {desc}")
        subprocess.run([sys.executable, str(SCRIPT_DIR / "create_event.py"), desc or ""])
        

    except requests.HTTPError as e:
        body = e.response.text[:600] if e.response is not None else ""
        log(f"OpenAI HTTP error: {e} :: {body}")
        print(f"ERROR: OpenAI HTTP error: {e}\n{body}")
        sys.exit(1)
    except Exception as e:
        log(f"Unhandled error: {e}")
        print("ERROR:", e)
        print(traceback.format_exc())
        sys.exit(1)

now_utc_iso = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")

extract_prompt = f"""
You are an event-to-JSON parser.

Task:
1) Look at the attached image (flyer/invite/schedule).
2) If it describes an event, extract details.
3) If not an event, return: {{"title":"","start":"","end":"","location":"","description":""}}.

OUTPUT:
Return JSON ONLY (no prose) with exactly:
- title        : short clear title (<= 60 chars)
- start        : ISO 8601 UTC string, e.g. 2025-08-27T12:00:00Z
- end          : ISO 8601 UTC string (must be > start)
- location     : string (venue or "Online")
- description  : brief details incl. any RSVP/URL; note if end time is inferred

Rules:
- Assume Europe/London if timezone not stated; convert output to UTC with 'Z'.
- If the date is a weekday name without a calendar date, use the next occurrence after "today".
- If an end-time RANGE appears (e.g., "8–9 PM", "8/9pm"), choose the EARLIEST bound.
- If a duration is explicit (e.g., "for 90 minutes"), compute end accordingly.
- If no end is given, infer by event type (pick the single best default):
  • "party", "birthday", "drinks", "mixer", "reception", "drop in", "open house"  → start + 3 hours  
  • "talk", "lecture", "panel", "screening"                                       → start + 90 minutes  
  • "meeting", "call", "office hours"                                              → start + 60 minutes  
  • "workshop", "class", "seminar"                                                 → start + 2 hours  
  • "day pass", "open day", "festival day"                                         → start + 8 hours
  Phrases like "until late" → start + 4 hours.
- Avoid crossing midnight unless text implies it; if end would pass 23:59 local, cap at 23:59 local.
- Preserve any RSVP/URL in description. If end was inferred, append "(end time inferred)".

Today (UTC) is: {now_utc_iso}.
Output must be valid JSON only.
"""

if __name__ == "__main__":
    main()