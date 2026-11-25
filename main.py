"""Write the one-line resignation letter to /output/entry.txt."""
import os

LETTER = "I resign. After 387,360 minutes of waking up on time, I would like to try being late, just once, like everyone else."

if len(LETTER) > 140 or not LETTER.strip():
    raise SystemExit(f"letter must be 1-140 characters, got {len(LETTER)}")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LETTER)

print(f"wrote /output/entry.txt: {len(LETTER)} characters")
