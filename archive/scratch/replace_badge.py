import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# I want to replace the space-y-sm div which contains the progress bars
pattern = re.compile(r'<div class="space-y-sm">.*?</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)

new_html = '''<div class="mt-md flex justify-start">
                                                        <img src="https://tryhackme-badges.s3.amazonaws.com/samihzs249.png" alt="TryHackMe Badge" class="h-10 object-contain hover:scale-105 transition-transform duration-300" />
                                                </div>'''

match = pattern.search(content)
if match:
    new_content = content[:match.start()] + new_html + content[match.end():]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Replaced progress bars with badge successfully.")
else:
    print("Pattern not found. Let's find it manually.")
    start_idx = content.find('<div class="space-y-sm">')
    print("start_idx:", start_idx)
    # The end of the block is 3 closing divs after "85%"
    pct_idx = content.find('85%', start_idx)
    end_idx = content.find('</div>', content.find('</div>', content.find('</div>', pct_idx) + 1) + 1) + 6
    if start_idx != -1 and pct_idx != -1:
        new_content = content[:start_idx] + new_html + content[end_idx:]
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Replaced using manual indexing!")
