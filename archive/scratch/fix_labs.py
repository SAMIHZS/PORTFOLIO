import re

try:
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    with open('index.html', 'r', encoding='utf-16') as f:
        content = f.read()

# Update TryHackMe rank and ranking stats
new_thm = """<!-- TryHackMe Progress (Spans 12 columns now since it's the only one) -->
                                <section
                                        class="md:col-span-12 max-w-4xl mx-auto w-full bg-surface-variant border border-outline-variant rounded-lg p-lg flex flex-col justify-between reveal">
                                        <div>
                                                <div class="flex items-center justify-between mb-md">
                                                        <h2
                                                                class="font-h3 text-h3 text-on-surface flex items-center gap-xs">
                                                                <span class="material-symbols-outlined text-primary">
                                                                        terminal
                                                                </span>
                                                                TryHackMe
                                                        </h2>
                                                        <span
                                                                class="flex items-center gap-1 font-label-sm text-label-sm text-secondary-container">
                                                                <span class="w-2 h-2 rounded-full bg-secondary">
                                                                </span>
                                                                Active
                                                        </span>
                                                </div>
                                                <div class="mb-sm">
                                                        <p
                                                                class="font-label-sm text-label-sm text-on-surface-variant uppercase tracking-wider mb-unit">
                                                                Current Rank
                                                        </p>
                                                        <p class="font-h2 text-h2 text-on-surface">
                                                                Pathfinder
                                                        </p>
                                                </div>
                                                <div class="space-y-sm">
                                                        <div>
                                                                <div
                                                                        class="flex justify-between font-label-sm text-label-sm mb-unit">
                                                                        <span class="text-on-surface">
                                                                                Jr Penetration Tester
                                                                        </span>
                                                                        <span class="text-primary">
                                                                                100%
                                                                        </span>
                                                                </div>
                                                                <div
                                                                        class="w-full bg-surface-container-highest rounded-full h-2">
                                                                        <div class="bg-primary h-2 rounded-full"
                                                                                style="width: 100%">
                                                                        </div>
                                                                </div>
                                                        </div>
                                                        <div>
                                                                <div
                                                                        class="flex justify-between font-label-sm text-label-sm mb-unit">
                                                                        <span class="text-on-surface">
                                                                                CompTIA Pentest+
                                                                        </span>
                                                                        <span class="text-primary">
                                                                                85%
                                                                        </span>
                                                                </div>
                                                                <div
                                                                        class="w-full bg-surface-container-highest rounded-full h-2">
                                                                        <div class="bg-primary h-2 rounded-full"
                                                                                style="width: 85%">
                                                                        </div>
                                                                </div>
                                                        </div>
                                                </div>
                                        </div>
                                        <div class="mt-md pt-sm border-t border-outline-variant flex items-center justify-between">
                                                <p class="font-code text-code text-on-surface-variant">
                                                        Top 35% Global Ranking • 10 Rooms
                                                </p>
                                                <a href="https://tryhackme.com/p/samihzs249?tab=completed-rooms" target="_blank" rel="noopener noreferrer" class="bg-primary text-on-primary font-label-sm text-label-sm px-md py-sm rounded hover:bg-inverse-primary hover:text-on-primary transition-colors flex items-center gap-2">
                                                    View Profile
                                                    <span class="material-symbols-outlined text-[16px]">open_in_new</span>
                                                </a>
                                        </div>
                                </section>"""

# Let's find the Grid container in Labs section
labs_start = content.find('<section class="py-xl reveal" id="labs">')
contact_start = content.find('<section class="py-xl reveal" id="contact">')

if labs_start != -1 and contact_start != -1:
    labs_section = content[labs_start:contact_start]
    
    # Inside labs_section, replace the grid content with new_thm
    grid_start = labs_section.find('<div class="grid grid-cols-1 md:grid-cols-12 gap-gutter">')
    if grid_start != -1:
        grid_end = labs_section.rfind('</div>\n                </section>')
        new_labs_section = labs_section[:grid_start + len('<div class="grid grid-cols-1 md:grid-cols-12 gap-gutter">')] + '\n' + new_thm + '\n                        ' + labs_section[grid_end:]
        content = content[:labs_start] + new_labs_section + content[contact_start:]
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated index.html Labs section")
    else:
        print("Could not find grid inside Labs")
else:
    print("Could not find Labs or Contact section")
