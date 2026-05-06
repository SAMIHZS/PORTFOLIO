# Shaik Sami Hassan – Cybersecurity Portfolio 🛡️

## 📝 Overview
A highly professional, responsive, and recruiter-friendly single-page cybersecurity portfolio website. This space showcases practical experience, technical projects, academic progress, and key industry certifications.

* **Live Website:** [https://samihzs.in](https://samihzs.in)
* **GitHub Repository:** [https://github.com/SAMIHZS/PORTFOLIO](https://github.com/SAMIHZS/PORTFOLIO)

---

## 🧭 Portfolio Sections
The single-page portfolio is neatly organized into the following segments:
- **About:** Personal introduction, career aspirations, and current educational focus.
- **Experience:** Chronological professional journey (Deloitte, SIH 2025, Cyber Intern, etc.).
- **Skills:** Categorized core competencies including defensive/offensive tools, VAPT, SOC, networks, and systems.
- **Projects:** Interactive list of curated open-source projects with active GitHub repository links.
- **Certifications:** Interactive lightbox gallery showcasing professional security achievements.
- **Achievements:** Academic highlights, hackathons, and TryHackMe platform status.
- **Contact:** Clean, functional contact options including LinkedIn, GitHub, email, and mobile.

---

## 🛠️ Tech Stack
* **HTML5:** Semantic architecture with modern SEO integration.
* **CSS3:** Vanilla Custom CSS paired with Tailwind CSS via CDN for rapid, responsive UI development.
* **JavaScript (ES6):** Interactivity, custom scroll-reveal animations, and lightbox gallery control.
* **Hosting Platform:** GitHub Pages with a custom domain setup.

---

## ✨ Features
* **Fully Responsive Design:** Tailored with mobile-first break points for seamless rendering across smartphones, tablets, and desktops.
* **Recruiter-Friendly UI:** Modern, readable, cybersecurity-themed dark-mode UI with high contrast and smooth micro-animations.
* **Interactive Certification Lightbox:** Click-to-zoom certification showcase with intuitive keyboard/mobile swipe control.
* **Dynamic TryHackMe Badge:** Integration of a live platform status badge highlighting current room accomplishments.
* **Resume Download:** Easily accessible View/Download buttons for direct resume access.
* **SEO & Meta Optimized:** Standard semantic tags, custom favicon, complete Open Graph, and Twitter Card support for maximum search engine discoverability.

---

## 🌟 Project Structure
```text
PORTFOLIO/
├── index.html                  # Main single-page application entry point
├── robots.txt                  # Production-ready search engine instructions
├── sitemap.xml                 # XML Sitemap for search engines
├── CNAME                       # Custom domain routing (samihzs.in)
│
├── assets/                     # Static assets directory
│   ├── css/
│   │   └── style.css           # Custom styles & overrides
│   ├── js/
│   │   └── script.js           # Lightweight dynamic animations & gallery logic
│   ├── images/
│   │   ├── certifications/     # Verified certification credential images
│   │   └── previews/           # Page preview screenshots for SEO OG cards
│   └── resume/
│       └── resume.pdf          # Professional candidate resume
│
├── sections/                   # Legacy modular HTML archive components
├── scripts/                    # Automation and validation utilities
└── archive/                    # Archived scratchpads and legacy scripts
```

---

## 💻 Local Development
To run this project locally without any dependencies:

### Step 1: Clone the repository
```bash
git clone https://github.com/SAMIHZS/PORTFOLIO.git
cd PORTFOLIO
```

### Step 2: Start a local server
Start a lightweight web server from the project root:

**Using Python (Recommended):**
```bash
python -m http.server 8000
```

**Using Node.js (Alternative):**
```bash
npm install -g local-server
local-server
```

### Step 3: Open in browser
Navigate to `http://localhost:8000` in your web browser.

---

## 🚀 Deployment Info
This portfolio is hosted for free using **GitHub Pages** integrated with a custom domain name:
* **Custom Domain:** `samihzs.in`
* **Routing:** Handled automatically by the root-level `CNAME` file.
* **SSL/HTTPS:** Provided and managed securely by GitHub Pages with automatically generated Let's Encrypt certificates.
