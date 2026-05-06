import os
import shutil

dirs = [
    'assets/css',
    'assets/js',
    'assets/images/certifications',
    'assets/images/projects',
    'assets/images/previews',
    'assets/images/icons',
    'assets/resume',
    'assets/docs',
    'sections',
    'scripts',
    'scripts/utilities',
    'archive/old_versions',
    'archive/unused',
    'archive/scratch'
]

for d in dirs:
    os.makedirs(d, exist_ok=True)

# File Moves
moves = []

# CSS & JS
if os.path.exists('style.css'): moves.append(('style.css', 'assets/css/style.css'))
if os.path.exists('script.js'): moves.append(('script.js', 'assets/js/script.js'))

# Certifications
if os.path.exists('assets/cert1.jpg'):
    for i in range(1, 9):
        if os.path.exists(f'assets/cert{i}.jpg'):
            moves.append((f'assets/cert{i}.jpg', f'assets/images/certifications/cert{i}.jpg'))

# Previews
for file in os.listdir('.'):
    if file.endswith('.png') and file != 'tryhackme-badges.png': # just in case
        moves.append((file, f'assets/images/previews/{file}'))

# Resume
resume_old = 'SHIAK SAMI HASSAN Cybersecurity Intern Resume.pdf'
if os.path.exists(resume_old):
    moves.append((resume_old, 'assets/resume/resume.pdf'))

# Legacy HTML
legacy_htmls = [
    '1-personal-portfolio.html',
    '2-projects-gallery.html',
    '3-certifications-showcase.html',
    '4-experience-timeline.html',
    '5-labs-and-research.html'
]
for html in legacy_htmls:
    if os.path.exists(html):
        moves.append((html, f'sections/{html[2:]}'))

# Scripts & Scratch
if os.path.exists('update_index.py'):
    moves.append(('update_index.py', 'scripts/update_index.py'))

if os.path.exists('scratch'):
    for f in os.listdir('scratch'):
        moves.append((f'scratch/{f}', f'archive/scratch/{f}'))

# Execute moves
for src, dst in moves:
    try:
        shutil.move(src, dst)
        print(f"Moved {src} -> {dst}")
    except Exception as e:
        print(f"Failed to move {src}: {e}")

# Clean up empty old scratch dir
if os.path.exists('scratch') and not os.listdir('scratch'):
    os.rmdir('scratch')
    print("Removed empty scratch directory")
