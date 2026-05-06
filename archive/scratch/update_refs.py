import os
import glob

# Gather all HTML files
html_files = ['index.html'] + glob.glob('sections/*.html')

for file in html_files:
    if not os.path.exists(file): continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply updates
    content = content.replace('href="style.css"', 'href="assets/css/style.css"')
    # In case there's ../ references for sections? Wait, the user accesses them from root, but if they are in sections/, their relative paths to assets/ might need to be ../assets/.
    # But wait, index.html is a single page application! The user doesn't navigate to the other HTML pages anymore. They are just archive/sections. Let's make paths relative to root or relative to the sections folder. 
    # Let's just do absolute-ish or root-relative paths for the HTML files in sections/ (e.g. `../assets/css/style.css`).
    
    if file.startswith('sections'):
        # For sections, assets is one level up
        content = content.replace('href="style.css"', 'href="../assets/css/style.css"')
        content = content.replace('src="script.js"', 'src="../assets/js/script.js"')
        content = content.replace('src="assets/cert', 'src="../assets/images/certifications/cert')
        content = content.replace('href="SHIAK SAMI HASSAN Cybersecurity Intern Resume.pdf"', 'href="../assets/resume/resume.pdf"')
        content = content.replace('href="SHIAK%20SAMI%20HASSAN%20Cybersecurity%20Intern%20Resume.pdf"', 'href="../assets/resume/resume.pdf"')
    else:
        content = content.replace('href="style.css"', 'href="assets/css/style.css"')
        content = content.replace('src="script.js"', 'src="assets/js/script.js"')
        content = content.replace('src="assets/cert', 'src="assets/images/certifications/cert')
        content = content.replace('href="SHIAK SAMI HASSAN Cybersecurity Intern Resume.pdf"', 'href="assets/resume/resume.pdf"')
        content = content.replace('href="SHIAK%20SAMI%20HASSAN%20Cybersecurity%20Intern%20Resume.pdf"', 'href="assets/resume/resume.pdf"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated references in {file}")
