import re

with open("scratch/reorder_timeline.py", "r", encoding="utf-8") as f:
    script_content = f.read()

# Extract new_timeline string from script
start = script_content.find('new_timeline = """') + len('new_timeline = """')
end = script_content.find('"""', start)
new_timeline = script_content[start:end]

with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

start_marker = "<!-- Timeline Item 1: Intern -->"
end_marker = "<!-- End Experience Section -->" # I'll use a better approach, find the end by looking for <section class="py-xl reveal" id="labs"> and backing up to the closing tags

start_idx = html_content.find(start_marker)
labs_idx = html_content.find('<section class="py-xl reveal" id="labs">', start_idx)

if start_idx != -1 and labs_idx != -1:
    # Find the closing tags before labs_idx
    # It should be something like </div>\n</div>\n</section>\n
    # Let's search backwards for </section> from labs_idx
    end_idx = html_content.rfind('</section>', start_idx, labs_idx)
    # Actually, the timeline items are inside a grid. Let's find the closing div of the grid, or just look for the last Timeline Item.
    
    # Let's search forwards for the end of the last timeline item
    # It ends with </div>\n      </div>\n     </div>
    # A safer way: just replace from start_idx to end_idx but keep the closing tags.
    # The new_timeline has ALL the timeline items including closing divs for themselves.
    # We just need to find where "Timeline Item 5: Hackathon" ends.
    last_item_start = html_content.find('<!-- Timeline Item 5: Hackathon -->', start_idx)
    # find the next timeline item or the end of the section container
    end_of_last_item = html_content.find('</section>', last_item_start)
    
    # We want to replace from start_idx to end_of_last_item (excluding </section>) with new_timeline
    # Wait, there are closing divs before </section>
    # In index.html:
    """
    <!-- Timeline Item 5: Hackathon -->
    ...
                                </div>
                        </div>
                </section>
                <section class="py-xl reveal" id="labs">
    """
    # Let's use re to replace everything between start_marker and </section>
    
    pattern = re.compile(r'(<!-- Timeline Item 1: Intern -->.*?)(?=\s*</div>\s*</div>\s*</section>\s*<section class="py-xl reveal" id="labs">)', re.DOTALL)
    
    match = pattern.search(html_content)
    if match:
        html_content = html_content[:match.start()] + new_timeline + html_content[match.end():]
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        print("Timeline fixed successfully!")
    else:
        print("Could not match the exact structure to replace. Trying a fallback...")
        # fallback
        pattern2 = re.compile(r'(<!-- Timeline Item 1: Intern -->.*?)(?=\s*</div>\s*</section>\s*<section class="py-xl reveal" id="labs">)', re.DOTALL)
        match2 = pattern2.search(html_content)
        if match2:
            html_content = html_content[:match2.start()] + new_timeline + html_content[match2.end():]
            with open("index.html", "w", encoding="utf-8") as f:
                f.write(html_content)
            print("Timeline fixed with fallback!")
        else:
            print("Fallback also failed.")
else:
    print("Could not find start or end markers")
