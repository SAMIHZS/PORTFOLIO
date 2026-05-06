# Cybersecurity Portfolio 🛡️

A sleek, responsive, single-page cybersecurity portfolio designed to highlight professional experience, technical projects, certifications, and active research.

## 🌟 Architecture & Structure

This repository has been professionally organized for scalability and ease of maintenance:

```text
/
├── index.html          # Main single-page application
├── robots.txt          # SEO rules
├── sitemap.xml         # SEO sitemap
├── CNAME               # Custom domain configuration (samihzs.in)
│
├── assets/             # Static resources
│   ├── css/            # Stylesheets (Vanilla CSS + Tailwind via CDN)
│   ├── js/             # Interactive logic
│   ├── images/         # Categorized images (certs, projects, icons, previews)
│   └── resume/         # Downloadable resume PDF
│
├── sections/           # Legacy/Modular HTML components
├── scripts/            # Automation and utility scripts
└── archive/            # Old versions and scratch files
```

## 🚀 Deployment

This project is fully static and production-ready.

### Deploying to GitHub Pages
1. Push the repository to GitHub.
2. Go to **Settings > Pages**.
3. Select the `main` branch as the source.
4. Add your custom domain (`samihzs.in`) if you haven't already.
5. Your portfolio is live!

### Deploying to Vercel or Netlify
1. Connect your GitHub repository to Vercel/Netlify.
2. No build command is required.
3. Set the output directory to the root (`/`).

## 🛠️ Local Development

To run this project locally, simply start a local web server in the root directory:

```bash
# Using Python 3
python -m http.server 8000
```

Then open your browser to `http://localhost:8000`.

## 🎨 Features
- **Responsive Design:** Mobile-first layout ensuring a seamless experience across all devices.
- **Dynamic Certificate Lightbox:** Click on any certification to view it in full size.
- **Integrated TryHackMe Stats:** Dynamically linked badge displaying live platform rank.
- **Scroll Reveal Animations:** Smooth content loading for a premium feel.
- **Cybersecurity Theme:** Dark mode optimized with high-contrast, modern aesthetics.

## 📝 Maintenance
- **Updating Resume:** Replace `assets/resume/resume.pdf` with your new file.
- **Updating Certifications:** Add images to `assets/images/certifications/` and update the grid in `index.html`.
- **CSS Framework:** Tailwind CSS is loaded via CDN. If you wish to build it locally in the future, initialize a `package.json` and install Tailwind CLI.
