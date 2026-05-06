import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all src and href
srcs = re.findall(r'src="([^"]+)"', content)
hrefs = re.findall(r'href="([^"]+)"', content)

missing = []

for link in srcs + hrefs:
    # Skip external links and anchors
    if link.startswith('http') or link.startswith('#') or link.startswith('mailto:'):
        continue
    
    # Path might be url encoded, like spaces to %20
    from urllib.parse import unquote
    local_path = unquote(link)
    
    # Remove query params or hashes if any
    local_path = local_path.split('?')[0].split('#')[0]
    
    if not os.path.exists(local_path):
        missing.append(link)

if missing:
    print("Found missing links:")
    for m in set(missing):
        print(m)
else:
    print("All local links in index.html are valid!")
