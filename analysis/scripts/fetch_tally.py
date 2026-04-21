"""
Download Tally form submissions to data/raw/.

Usage:
    uv run python analysis/scripts/fetch_tally.py

Requires .env with:
    TALLY_API_KEY=...
    TALLY_FORM_ID_ES=q4EQX9
    TALLY_FORM_ID_EN=...   (optional)
"""

import os
import json
from datetime import datetime
from pathlib import Path

import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["TALLY_API_KEY"]
BASE_URL = "https://api.tally.so"
RAW_DIR = Path(__file__).parents[2] / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)


def fetch_submissions(form_id: str) -> list[dict]:
    headers = {"Authorization": f"Bearer {API_KEY}"}
    submissions = []
    page = 1

    while True:
        resp = httpx.get(
            f"{BASE_URL}/forms/{form_id}/submissions",
            headers=headers,
            params={"page": page, "limit": 200},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        batch = data.get("submissions", [])
        submissions.extend(batch)
        if len(batch) < 200:
            break
        page += 1

    return submissions


def save(form_id: str, submissions: list[dict]) -> Path:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = RAW_DIR / f"submissions_{form_id}_{ts}.json"
    out.write_text(json.dumps(submissions, ensure_ascii=False, indent=2))
    return out


def main():
    for env_var in ("TALLY_FORM_ID_ES", "TALLY_FORM_ID_EN"):
        form_id = os.environ.get(env_var, "").strip()
        if not form_id:
            continue
        print(f"Fetching {env_var} ({form_id})...")
        subs = fetch_submissions(form_id)
        path = save(form_id, subs)
        print(f"  {len(subs)} submissions -> {path}")


if __name__ == "__main__":
    main()
