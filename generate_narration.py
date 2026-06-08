"""Generera per-slide-uppläsning för kursbiblioteket via ElevenLabs v3.

Läser narration/<kurs>.<språk>.json ({ "1": "text", ... }) och skriver
<kurs>/audio/narration/<språk>/slide-<n>.mp3. Hoppar filer som redan finns
(om inte --force). Samma klonade röst läser alla språk.

Kör:
  ELEVEN_KEY=$(cat ~/.config/elevenlabs/api-key) \
  python3 generate_narration.py --voice <VOICE_ID> [--course forlossning] [--lang sv] [--force]
"""
import argparse, glob, json, os, sys, time, urllib.request
from pathlib import Path

ROOT = Path(__file__).parent
KEY = os.environ.get("ELEVEN_KEY") or Path.home().joinpath(".config/elevenlabs/api-key").read_text().strip()

def gen(voice, text):
    body = json.dumps({"text": text, "model_id": "eleven_v3",
                       "voice_settings": {"stability": 0.5, "similarity_boost": 0.9,
                                          "use_speaker_boost": True}}).encode()
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice}?output_format=mp3_44100_128",
        data=body, headers={"xi-api-key": KEY, "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req) as r:
        return r.read()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--voice", required=True, help="ElevenLabs voice id (Maries klon)")
    ap.add_argument("--course", help="bara denna kurs (forlossning/amning)")
    ap.add_argument("--lang", help="bara detta språk (sv/en/ar/so/fa)")
    ap.add_argument("--force", action="store_true", help="skriv över befintliga klipp")
    a = ap.parse_args()

    files = sorted(glob.glob(str(ROOT / "narration" / "*.*.json")))
    done = skipped = failed = 0
    for f in files:
        stem = Path(f).name[:-5]              # e.g. "forlossning.sv"
        course, lang = stem.rsplit(".", 1)
        if a.course and course != a.course: continue
        if a.lang and lang != a.lang: continue
        scripts = json.loads(Path(f).read_text())
        outdir = ROOT / course / "audio" / "narration" / lang
        outdir.mkdir(parents=True, exist_ok=True)
        print(f"== {course} / {lang} ({len(scripts)} slides) ==")
        for n, text in scripts.items():
            out = outdir / f"slide-{n}.mp3"
            if out.exists() and not a.force:
                skipped += 1; continue
            for attempt in range(3):
                try:
                    out.write_bytes(gen(a.voice, text)); print(f"  OK slide-{n}"); done += 1; break
                except urllib.error.HTTPError as e:
                    print(f"  retry slide-{n}: {e.code} {e.read().decode()[:160]}"); time.sleep(4)
                except Exception as e:
                    print(f"  retry slide-{n}: {e}"); time.sleep(4)
            else:
                failed += 1
            time.sleep(0.5)
    print(f"\nKlart. genererade={done} hoppade={skipped} misslyckade={failed}")

if __name__ == "__main__":
    main()
