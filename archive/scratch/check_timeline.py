import re
with open("index.html", "r", encoding="utf-8") as f: content = f.read()
timeline = re.findall(r'<h3[^>]*>([^<]+)</h3>', content)
print('Headers:', [t.strip() for t in timeline])
