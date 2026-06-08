import asyncio, json, sys
from pathlib import Path
SKILL = Path("/Users/christoffersundberg/Projects/glaseyewear/content/.claude/skills/aicontentgenerator")
sys.path.insert(0, str(SKILL))
from services import gemini
MODEL="gemini-3-pro-image-preview"
ROOT=Path("/Users/christoffersundberg/Projects/foraldrakurser")
STYLE=("Soft, tender hand-painted gouache-style illustration, warm calm reassuring mood, "
 "limited palette of warm cream, terracotta, soft blush pink, sage green, muted gold ochre, "
 "gentle rounded organic shapes, soft edges, painterly, generous negative space, tasteful and non-clinical. "
 "NO text, no letters, no numbers. ")
slugs=["nyfodda","backenbotten","profylax","kejsarsnitt","foralder-tillsammans","psykisk-halsa","hlr-sakerhet","mat-introduktion"]
jobs=[]
for s in slugs:
    f=ROOT/s/"_images.json"
    if not f.exists(): continue
    for it in json.loads(f.read_text()):
        jobs.append((s, it["name"], it["prompt"]))
print(f"{len(jobs)} images")
sem=asyncio.Semaphore(4)
async def one(slug,name,prompt):
    out=ROOT/slug/"images"/f"{name}.png"
    if out.exists(): print("skip",slug,name); return
    p = prompt if prompt.strip().lower().startswith("soft") else STYLE+prompt
    async with sem:
        for a in range(3):
            try:
                img=await gemini.generate_image(model=MODEL,prompt=p,aspect_ratio="3:4",image_size="2K")
                out.parent.mkdir(parents=True,exist_ok=True); img.save(out); print("OK",slug,name); return
            except Exception as e:
                print("retry",slug,name,str(e)[:80]); await asyncio.sleep(3)
        print("FAIL",slug,name)
async def main():
    await asyncio.gather(*(one(s,n,p) for s,n,p in jobs))
    print(f"cost ${gemini.get_cost_estimate():.2f}")
asyncio.run(main())
