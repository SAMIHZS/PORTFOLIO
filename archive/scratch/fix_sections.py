import os
from bs4 import BeautifulSoup

base_dir = "E:\\project\\PORTFOLIO"
index_path = os.path.join(base_dir, "index.html")
p1_path = os.path.join(base_dir, "1-personal-portfolio.html")

with open(index_path, "r", encoding="utf-8") as f:
    soup_idx = BeautifulSoup(f.read(), "html.parser")

with open(p1_path, "r", encoding="utf-8") as f:
    soup1 = BeautifulSoup(f.read(), "html.parser")

main = soup_idx.find("main")

# Find sections in p1
home_sec = soup1.find("section", id="home")
about_sec = soup1.find("section", id="about")

if home_sec:
    # Update Hero Data before inserting
    h1 = home_sec.find("h1")
    if h1:
        h1.string = "SAMI HZS"
        h1.name = "h1"
    h2 = home_sec.find("h2")
    if h2:
        h2.string = "Cybersecurity Student | Security Researcher | Future Security Engineer"
    
    # Fix links
    for btn in home_sec.find_all("button"):
        text = btn.text.strip()
        new_a = soup_idx.new_tag("a", href="assets/SHAIKSAMIHASSANRESUME_compressed.pdf")
        new_a["class"] = btn.get("class", [])
        if "View Resume" in text:
            new_a["target"] = "_blank"
            new_a.append(btn.contents[0])
            new_a.append("View Resume")
        elif "Download Resume" in text:
            new_a["download"] = ""
            new_a.append(btn.contents[0])
            new_a.append("Download Resume")
        else:
            continue
        btn.replace_with(new_a)
    
    # Add reveal class
    classes = home_sec.get("class", [])
    if "reveal" not in classes:
        classes.append("reveal")
    home_sec["class"] = classes
    
    # Insert at beginning of main
    main.insert(0, home_sec)

if about_sec:
    # Change h1 to h2 inside about
    for h1 in about_sec.find_all("h1"):
        h1.name = "h2"
        h1["class"] = [c.replace("h1", "h2") for c in h1.get("class", [])]
        
    # Add reveal class
    classes = about_sec.get("class", [])
    if "reveal" not in classes:
        classes.append("reveal")
    about_sec["class"] = classes
    
    # Insert after home
    if home_sec:
        home_sec.insert_after(about_sec)
    else:
        main.insert(0, about_sec)

# Fix images
for img in main.find_all("img"):
    img["loading"] = "lazy"

with open(index_path, "w", encoding="utf-8") as f:
    f.write(soup_idx.prettify())

print("Successfully injected missing sections.")
