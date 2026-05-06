import re

with open('e:/project/PORTFOLIO/4-experience-timeline.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_timeline = """<!-- Timeline Item 1: Education -->
<div class="relative flex flex-col md:flex-row items-center md:justify-between mb-xl">
<!-- Timeline Dot -->
<div class="absolute left-[-5px] md:left-1/2 md:-ml-2 w-4 h-4 rounded-full bg-surface-dim border-2 border-secondary z-10"></div>
<!-- Content (Left Side Desktop, Right Side Mobile) -->
<div class="w-full md:w-5/12 pl-lg md:pl-0 md:pr-lg md:text-right">
<div class="bg-surface-container-low border border-surface-variant p-md rounded-lg hover:border-secondary transition-colors duration-200">
<div class="flex items-center md:justify-end gap-xs mb-xs">
<span class="material-symbols-outlined text-secondary text-xl">school</span>
<h3 class="font-h3 text-h3 text-on-surface">BCA (Honours) Student</h3>
</div>
<p class="font-label-sm text-label-sm text-secondary mb-sm">Academic Institution • 2024 - Present</p>
<p class="font-body-md text-body-md text-on-surface-variant mb-md">
                            Pursuing advanced studies in computer applications with a strong foundation in programming, systems architecture, and foundational security concepts.
                        </p>
<div class="flex flex-wrap gap-xs md:justify-end">
<span class="bg-surface-container-highest px-2 py-1 rounded text-label-sm font-label-sm text-on-surface">Computer Science</span>
<span class="bg-surface-container-highest px-2 py-1 rounded text-label-sm font-label-sm text-on-surface">Architecture</span>
</div>
</div>
</div>
<!-- Spacer for right side on Desktop -->
<div class="hidden md:block w-5/12"></div>
</div>
<!-- Timeline Item 2: Deloitte -->
<div class="relative flex flex-col md:flex-row items-center md:justify-between mb-xl">
<!-- Timeline Dot -->
<div class="absolute left-[-5px] md:left-1/2 md:-ml-2 w-4 h-4 rounded-full bg-surface-dim border-2 border-primary z-10"></div>
<!-- Spacer for left side on Desktop -->
<div class="hidden md:block w-5/12"></div>
<!-- Content (Right Side Desktop & Mobile) -->
<div class="w-full md:w-5/12 pl-lg md:pl-lg">
<div class="bg-surface-container-low border border-surface-variant p-md rounded-lg hover:border-primary transition-colors duration-200">
<div class="flex items-center gap-xs mb-xs">
<span class="material-symbols-outlined text-primary text-xl">work</span>
<h3 class="font-h3 text-h3 text-on-surface">Deloitte Cyber Job Simulation</h3>
</div>
<p class="font-label-sm text-label-sm text-primary mb-sm">Forage • 2024</p>
<p class="font-body-md text-body-md text-on-surface-variant mb-md">
                            Completed practical tasks in cybersecurity operations, threat analysis, and risk mitigation simulating a real-world corporate environment.
                        </p>
<div class="flex flex-wrap gap-xs">
<span class="bg-surface-container-highest px-2 py-1 rounded text-label-sm font-label-sm text-on-surface">Threat Analysis</span>
<span class="bg-surface-container-highest px-2 py-1 rounded text-label-sm font-label-sm text-on-surface">Risk Mitigation</span>
</div>
</div>
</div>
</div>
<!-- Timeline Item 3: Leadership -->
<div class="relative flex flex-col md:flex-row items-center md:justify-between mb-xl">
<!-- Timeline Dot -->
<div class="absolute left-[-5px] md:left-1/2 md:-ml-2 w-4 h-4 rounded-full bg-surface-dim border-2 border-tertiary-container z-10"></div>
<!-- Content (Left Side Desktop, Right Side Mobile) -->
<div class="w-full md:w-5/12 pl-lg md:pl-0 md:pr-lg md:text-right">
<div class="bg-surface-container-low border border-surface-variant p-md rounded-lg hover:border-tertiary-container transition-colors duration-200">
<div class="flex items-center md:justify-end gap-xs mb-xs">
<span class="material-symbols-outlined text-tertiary-container text-xl">groups</span>
<h3 class="font-h3 text-h3 text-on-surface">SIH 2025 Team Leader</h3>
</div>
<p class="font-label-sm text-label-sm text-tertiary-container mb-sm">Hackathon Participant • 2024 - 2025</p>
<p class="font-body-md text-body-md text-on-surface-variant mb-md">
                            Led a cross-functional team in the Smart India Hackathon, driving project ideation, technical architecture design, and final implementation delivery under strict deadlines.
                        </p>
<div class="flex flex-wrap gap-xs md:justify-end">
<span class="bg-surface-container-highest px-2 py-1 rounded text-label-sm font-label-sm text-on-surface">Leadership</span>
<span class="bg-surface-container-highest px-2 py-1 rounded text-label-sm font-label-sm text-on-surface">Project Management</span>
</div>
</div>
</div>
<!-- Spacer for right side on Desktop -->
<div class="hidden md:block w-5/12"></div>
</div>
<!-- Timeline Item 4: Hackathon -->
<div class="relative flex flex-col md:flex-row items-center md:justify-between mb-xl">
<!-- Timeline Dot -->
<div class="absolute left-[-5px] md:left-1/2 md:-ml-2 w-4 h-4 rounded-full bg-surface-dim border-2 border-secondary z-10"></div>
<!-- Spacer for left side on Desktop -->
<div class="hidden md:block w-5/12"></div>
<!-- Content (Right Side Desktop & Mobile) -->
<div class="w-full md:w-5/12 pl-lg md:pl-lg">
<div class="bg-surface-container-low border border-surface-variant p-md rounded-lg hover:border-secondary transition-colors duration-200">
<div class="flex items-center gap-xs mb-xs">
<span class="material-symbols-outlined text-secondary text-xl">event</span>
<h3 class="font-h3 text-h3 text-on-surface">24 Hour Hackathon</h3>
</div>
<p class="font-label-sm text-label-sm text-secondary mb-sm">Participant • 2024</p>
<p class="font-body-md text-body-md text-on-surface-variant mb-md">
                            Collaborated in a high-pressure 24-hour hackathon, rapidly prototyping and deploying innovative solutions.
                        </p>
<div class="flex flex-wrap gap-xs">
<span class="bg-surface-container-highest px-2 py-1 rounded text-label-sm font-label-sm text-on-surface">Rapid Prototyping</span>
<span class="bg-surface-container-highest px-2 py-1 rounded text-label-sm font-label-sm text-on-surface">Teamwork</span>
</div>
</div>
</div>
</div>
<!-- Timeline Item 5: Intern -->
<div class="relative flex flex-col md:flex-row items-center md:justify-between mb-xl">
<!-- Timeline Dot -->
<div class="absolute left-[-5px] md:left-1/2 md:-ml-2 w-4 h-4 rounded-full bg-surface-dim border-2 border-primary z-10"></div>
<!-- Content (Left Side Desktop, Right Side Mobile) -->
<div class="w-full md:w-5/12 pl-lg md:pl-0 md:pr-lg md:text-right">
<div class="bg-surface-container-low border border-surface-variant p-md rounded-lg hover:border-primary transition-colors duration-200">
<div class="flex items-center md:justify-end gap-xs mb-xs">
<span class="material-symbols-outlined text-primary text-xl">security</span>
<h3 class="font-h3 text-h3 text-on-surface">Cyber Security Intern</h3>
</div>
<p class="font-label-sm text-label-sm text-primary mb-sm">Future Interns • April 2026 - Present</p>
<p class="font-body-md text-body-md text-on-surface-variant mb-md">
                            Specializing in reconnaissance, technical analysis, and developing comprehensive security documentation within enterprise Linux environments.
                        </p>
<div class="flex flex-wrap gap-xs md:justify-end">
<span class="bg-surface-container-highest px-2 py-1 rounded text-label-sm font-label-sm text-on-surface">Linux</span>
<span class="bg-surface-container-highest px-2 py-1 rounded text-label-sm font-label-sm text-on-surface">Reconnaissance</span>
<span class="bg-surface-container-highest px-2 py-1 rounded text-label-sm font-label-sm text-on-surface">Analysis</span>
</div>
</div>
</div>
<!-- Spacer for right side on Desktop -->
<div class="hidden md:block w-5/12"></div>
</div>"""

pattern = re.compile(r'(<!-- Timeline Item 1: Intern -->)(.*?)(<!-- Spacer for right side on Desktop -->\n<div class="hidden md:block w-5/12"></div>\n</div>)', re.DOTALL)

if pattern.search(content):
    new_content = pattern.sub(new_timeline, content)
    with open('e:/project/PORTFOLIO/4-experience-timeline.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Timeline updated successfully in 4-experience-timeline.html.")
else:
    print("Pattern not found!")
