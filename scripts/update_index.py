import os
from bs4 import BeautifulSoup

file_path = "E:\\project\\PORTFOLIO\\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

# 1. Update Navigation
nav = soup.find("nav")
nav["id"] = "navbar"

# Add Hamburger button for mobile
flex_container = nav.find("div", class_="flex justify-between items-center max-w-7xl mx-auto px-6 h-16 w-full max-w-[1200px]")

# Hamburger icon HTML
hamburger_html = """
<button id="navToggle" class="md:hidden text-slate-400 hover:text-slate-100 focus:outline-none transition-colors" aria-expanded="false">
    <span class="material-symbols-outlined text-3xl">menu</span>
</button>
"""
hamburger_soup = BeautifulSoup(hamburger_html, "html.parser")
flex_container.append(hamburger_soup)

# Modify desktop nav links container to be the mobile menu as well
nav_links_container = nav.find("div", class_="hidden md:flex gap-md items-center")
nav_links_container["id"] = "navMenu"
# Keep desktop styles, but we will control mobile styles via CSS or JS. 
# We'll just change the class to allow mobile menu styling in CSS.
nav_links_container["class"] = "nav-menu hidden md:flex gap-md items-center flex-col md:flex-row absolute md:relative top-16 md:top-0 left-0 w-full md:w-auto bg-slate-950/95 md:bg-transparent p-6 md:p-0 border-b border-slate-800 md:border-none shadow-lg md:shadow-none"

# Add nav-link class to all nav links for JS tracking
for a in nav_links_container.find_all("a"):
    classes = a.get("class", [])
    if "nav-link" not in classes:
        classes.append("nav-link")
    a["class"] = classes

# 2. Update Hero Section
hero = soup.find("section", id="home")
if hero:
    h1 = hero.find("h1")
    if h1:
        h1.string = "SAMI HZS"
    h2 = hero.find("h2")
    if h2:
        h2.string = "Cybersecurity Student | Security Researcher | Future Security Engineer"

    # Fix buttons in hero
    for a in hero.find_all("a"):
        text = a.text.strip()
        if "Resume" in text:
            a["href"] = "assets/SHAIKSAMIHASSANRESUME_compressed.pdf" # Assuming in assets or root, let's keep it root or assets. User said "Resume PDF" is in assets or root. I'll use "SHAIKSAMIHASSANRESUME_compressed.pdf"
            a["target"] = "_blank"

# 3. Certifications Integration
cert_section = soup.find("section", id="certifications")
if cert_section:
    articles = cert_section.find_all("article")
    cert_images = ["assets/cert1.jpg", "assets/cert2.jpg", "assets/cert3.jpg", "assets/cert4.jpg", "assets/cert5.jpg"]
    
    for i, article in enumerate(articles):
        if i < len(cert_images):
            img = article.find("img")
            if img:
                img["src"] = cert_images[i]
                img["loading"] = "lazy"
            
            # Make the whole card clickable for lightbox, or the button
            btn = article.find("button")
            if btn:
                btn["class"] = btn.get("class", []) + ["cert-btn"]
                btn["data-cert-index"] = str(i)
                btn.string = ""
                btn.append("View Certificate")
                span = soup.new_tag("span", **{"class": "material-symbols-outlined text-[16px]"})
                span.string = "zoom_in"
                btn.append(span)
                
            article["class"] = article.get("class", []) + ["cert-card", "cursor-pointer"]
            article["data-cert-index"] = str(i)
        else:
            article.decompose() # Remove the 6th certificate since there are only 5

# 4. Projects Integration
proj_section = soup.find("section", id="projects")
if proj_section:
    articles = proj_section.find_all("article")
    for article in articles:
        # Just ensure the github link is somewhat realistic
        links = article.find_all("a")
        for link in links:
            if "GitHub" in link.text:
                link["href"] = "https://github.com/SAMIHZS"
                link["target"] = "_blank"

# 5. Add Lightbox Modal to body
modal_html = """
<div id="certModal" class="fixed inset-0 z-[100] hidden bg-black/90 backdrop-blur-sm flex items-center justify-center opacity-0 transition-opacity duration-300">
    <div class="relative w-full max-w-5xl p-4 flex flex-col items-center">
        <button id="closeModal" class="absolute top-4 right-4 text-white hover:text-primary transition-colors bg-black/50 p-2 rounded-full">
            <span class="material-symbols-outlined text-3xl">close</span>
        </button>
        
        <div class="relative flex items-center justify-center w-full">
            <button id="prevCert" class="absolute left-0 md:-left-12 text-white hover:text-primary p-2 bg-black/50 rounded-full transition-colors hidden md:block">
                <span class="material-symbols-outlined text-4xl">chevron_left</span>
            </button>
            
            <img id="modalImg" src="" alt="Certificate" class="max-h-[85vh] w-auto max-w-full object-contain rounded border border-[#334155] shadow-2xl transition-transform duration-300 cursor-zoom-in" />
            
            <button id="nextCert" class="absolute right-0 md:-right-12 text-white hover:text-primary p-2 bg-black/50 rounded-full transition-colors hidden md:block">
                <span class="material-symbols-outlined text-4xl">chevron_right</span>
            </button>
        </div>
        
        <div class="flex justify-between w-full md:hidden mt-4 px-8">
             <button id="prevCertMob" class="text-white hover:text-primary p-2 bg-slate-800 rounded-full transition-colors">
                <span class="material-symbols-outlined text-3xl">chevron_left</span>
            </button>
            <button id="nextCertMob" class="text-white hover:text-primary p-2 bg-slate-800 rounded-full transition-colors">
                <span class="material-symbols-outlined text-3xl">chevron_right</span>
            </button>
        </div>
    </div>
</div>
"""
modal_soup = BeautifulSoup(modal_html, "html.parser")
soup.body.append(modal_soup)

# Add reveal classes to sections
for section in soup.find_all("section"):
    classes = section.get("class", [])
    if "reveal" not in classes:
        classes.append("reveal")
    section["class"] = classes

# Link the script.js at the end of body
script_tag = soup.new_tag("script", src="script.js")
soup.body.append(script_tag)

# Link style.css in head
link_tag = soup.new_tag("link", rel="stylesheet", href="style.css")
soup.head.append(link_tag)

# Update all images to have loading="lazy"
for img in soup.find_all("img"):
    img["loading"] = "lazy"

with open(file_path, "w", encoding="utf-8") as f:
    f.write(soup.prettify())

print("Successfully updated index.html!")
