/* ============================================================
   PORTFOLIO – script.js
   Handles UX features: Mobile Menu, Scroll Reveal, Active Nav,
   and Certificate Lightbox.
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {
    
    // --- 1. Mobile Menu Toggle ---
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');
    const navLinks = document.querySelectorAll('.nav-link');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            const isOpen = navMenu.classList.toggle('open');
            navToggle.setAttribute('aria-expanded', isOpen);
        });

        // Close menu on link click
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('open');
                navToggle.setAttribute('aria-expanded', 'false');
            });
        });

        // Close on outside click
        document.addEventListener('click', (e) => {
            if (navMenu.classList.contains('open') && !navMenu.contains(e.target) && !navToggle.contains(e.target)) {
                navMenu.classList.remove('open');
                navToggle.setAttribute('aria-expanded', 'false');
            }
        });
    }

    // --- 2. Scroll Reveal Animations ---
    const revealElements = document.querySelectorAll('.reveal');
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target); // Only reveal once
            }
        });
    }, { rootMargin: "0px 0px -50px 0px" });

    revealElements.forEach(el => revealObserver.observe(el));

    // --- 3. Active Nav Highlighting ---
    const sections = document.querySelectorAll('section[id]');
    
    function highlightNav() {
        const scrollY = window.scrollY + 150;
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');
            
            if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${sectionId}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }
    
    window.addEventListener('scroll', highlightNav, { passive: true });
    highlightNav(); // Initial call

    // --- 4. Certificate Lightbox ---
    const certImages = [
        "assets/images/certifications/cert1.jpg",
        "assets/images/certifications/cert2.jpg",
        "assets/images/certifications/cert3.jpg",
        "assets/images/certifications/cert4.jpg",
        "assets/images/certifications/cert5.jpg"
    ];
    let currentCertIndex = 0;

    const certModal = document.getElementById('certModal');
    const modalImg = document.getElementById('modalImg');
    const closeBtn = document.getElementById('closeModal');
    
    const prevBtn = document.getElementById('prevCert');
    const nextBtn = document.getElementById('nextCert');
    const prevBtnMob = document.getElementById('prevCertMob');
    const nextBtnMob = document.getElementById('nextCertMob');

    const certCards = document.querySelectorAll('.cert-card');

    function openModal(index) {
        currentCertIndex = parseInt(index);
        updateModalImage();
        certModal.classList.remove('hidden');
        // Small delay to allow display:block to apply before changing opacity
        setTimeout(() => {
            certModal.classList.remove('opacity-0');
        }, 10);
        document.body.style.overflow = 'hidden'; // Prevent scrolling
        modalImg.classList.remove('cert-zoom'); // Reset zoom
    }

    function closeModalFunc() {
        certModal.classList.add('opacity-0');
        setTimeout(() => {
            certModal.classList.add('hidden');
        }, 300);
        document.body.style.overflow = ''; // Restore scrolling
    }

    function updateModalImage() {
        if (currentCertIndex < 0) currentCertIndex = certImages.length - 1;
        if (currentCertIndex >= certImages.length) currentCertIndex = 0;
        modalImg.src = certImages[currentCertIndex];
    }

    // Attach click listeners to cards
    certCards.forEach(card => {
        card.addEventListener('click', function(e) {
            // Prevent opening if they clicked the "Verify Credential" link directly
            // unless we want it to open the lightbox too. We'll open lightbox.
            e.preventDefault();
            const index = this.getAttribute('data-cert-index');
            openModal(index);
        });
    });

    if (closeBtn) closeBtn.addEventListener('click', closeModalFunc);
    
    // Background click to close
    if (certModal) {
        certModal.addEventListener('click', (e) => {
            if (e.target === certModal) closeModalFunc();
        });
    }

    // Navigation buttons
    function nextImage(e) {
        e.stopPropagation();
        currentCertIndex++;
        updateModalImage();
        modalImg.classList.remove('cert-zoom');
    }
    
    function prevImage(e) {
        e.stopPropagation();
        currentCertIndex--;
        updateModalImage();
        modalImg.classList.remove('cert-zoom');
    }

    if (nextBtn) nextBtn.addEventListener('click', nextImage);
    if (prevBtn) prevBtn.addEventListener('click', prevImage);
    if (nextBtnMob) nextBtnMob.addEventListener('click', nextImage);
    if (prevBtnMob) prevBtnMob.addEventListener('click', prevImage);

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (certModal && !certModal.classList.contains('hidden')) {
            if (e.key === 'Escape') closeModalFunc();
            if (e.key === 'ArrowRight') nextImage(e);
            if (e.key === 'ArrowLeft') prevImage(e);
        }
    });

    // Zoom functionality
    if (modalImg) {
        modalImg.addEventListener('click', (e) => {
            e.stopPropagation();
            modalImg.classList.toggle('cert-zoom');
        });
    }

    // Add typing cursor to hero
    const whoami = document.querySelector('.font-code.text-primary');
    if (whoami) {
        whoami.classList.add('typing-cursor');
    }
});
