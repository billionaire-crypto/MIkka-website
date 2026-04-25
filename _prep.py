"""Clean the two .txt HTML files (fix smart quotes, en-dashes, stray hyphens)
and write hero_page_clean.html + awards_page_clean.html + index.html."""
import os, re, pathlib

ROOT = pathlib.Path(r"C:\Users\kyawz\Mikka website")

def clean(text: str) -> str:
    # Smart quotes -> straight
    text = text.replace("\u2018", "'").replace("\u2019", "'")
    text = text.replace("\u201C", '"').replace("\u201D", '"')
    # En/em dashes in CSS var(--x) and -- sequences
    text = text.replace("\u2013", "--").replace("\u2014", "--")
    # NBSP -> space
    text = text.replace("\u00A0", " ")
    # Leading "- {" on its own line should be "* {"
    text = re.sub(r"(?m)^-(\s*\{)", r"*\1", text)
    return text

def process(src_name: str, out_name: str) -> pathlib.Path:
    src = ROOT / src_name
    out = ROOT / out_name
    raw = src.read_text(encoding="utf-8", errors="replace")
    out.write_text(clean(raw), encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")
    return out

hero = process("HERO PAGE CLEAN CODE.txt", "hero_page_clean.html")
awards = process("AWARD PAGE CLEAN CODE.txt", "awards_page_clean.html")

# Simple index with links + iframe preview
index = ROOT / "index.html"
index.write_text("""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mikka Chinbaatar -- Preview</title>
<style>
  :root { --bg:#F5E4DC; --ink:#2A1528; --accent:#C44860; --muted:#6E3E5A; }
  html,body{margin:0;padding:0;background:var(--bg);color:var(--ink);
    font-family:'IBM Plex Mono',ui-monospace,monospace}
  header{padding:18px 24px;border-bottom:1px solid rgba(42,21,40,.15);
    display:flex;gap:24px;align-items:center;flex-wrap:wrap}
  header h1{margin:0;font:600 14px/1 'IBM Plex Mono',monospace;letter-spacing:.14em;text-transform:uppercase}
  header a{color:var(--accent);text-decoration:none;font-size:12px;letter-spacing:.1em;text-transform:uppercase}
  header a:hover{color:var(--ink);text-decoration:underline}
  main{display:block}
  iframe{display:block;width:100%;border:0;background:var(--bg)}
  .frame-wrap{border-bottom:2px solid rgba(42,21,40,.1)}
  .frame-wrap h2{margin:0;padding:10px 24px;font:600 11px/1.4 'IBM Plex Mono',monospace;
    letter-spacing:.18em;text-transform:uppercase;color:var(--muted);
    background:rgba(42,21,40,.04)}
</style></head>
<body>
<header>
  <h1>Mikka -- Live Preview</h1>
  <a href="hero_page_clean.html" target="_blank">Open hero standalone</a>
  <a href="awards_page_clean.html" target="_blank">Open awards standalone</a>
</header>
<main>
  <div class="frame-wrap">
    <h2>01 -- Hero</h2>
    <iframe src="hero_page_clean.html" style="height:100vh"></iframe>
  </div>
  <div class="frame-wrap">
    <h2>02 -- Awards & Distinctions</h2>
    <iframe src="awards_page_clean.html" style="height:160vh"></iframe>
  </div>
</main>
</body></html>
""", encoding="utf-8")
print(f"wrote {index}")
