// Mobile hamburger menu toggle
(function () {
    const btn = document.getElementById('hamburger-btn');
    const menu = document.getElementById('mobile-menu');
    const icon = document.getElementById('hamburger-icon');

    if (!btn || !menu) return;

    function setMenuState(open) {
        menu.classList.toggle('hidden', !open);
        menu.classList.toggle('open', open);
        menu.setAttribute('aria-hidden', open ? 'false' : 'true');
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');

        if (icon) {
            icon.textContent = open ? 'close' : 'menu';
        }
    }

    btn.addEventListener('click', function () {
        setMenuState(!menu.classList.contains('open'));
    });

    menu.querySelectorAll('a').forEach(function (link) {
        link.addEventListener('click', function () {
            setMenuState(false);
        });
    });

    document.addEventListener('click', function (event) {
        if (!menu.contains(event.target) && !btn.contains(event.target)) {
            setMenuState(false);
        }
    });

    window.addEventListener('resize', function () {
        if (window.innerWidth >= 1024) {
            setMenuState(false);
        }
    });

    setMenuState(false);
})();

// Smart Navbar functionality
(function () {
    const navbar = document.querySelector('nav');
    const desktopNavLinks = document.getElementById('desktop-nav-links');
    const mobileMenuItems = document.querySelectorAll('.mobile-menu-item');
    
    if (!navbar) return;

    // Scroll threshold for navbar changes
    const scrollThreshold = 50;
    let lastScrollY = window.scrollY;
    let ticking = false;

    // Update navbar state based on scroll
    function updateNavbarState() {
        const currentScrollY = window.scrollY;
        
        // Add/remove scrolled classes
        if (currentScrollY > scrollThreshold) {
            navbar.classList.add('navbar-scrolled', 'navbar-glass-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled', 'navbar-glass-scrolled');
        }
        
        lastScrollY = currentScrollY;
        ticking = false;
    }

    // Throttled scroll handler
    function onScroll() {
        if (!ticking) {
            requestAnimationFrame(updateNavbarState);
            ticking = true;
        }
    }

    // Active section detection
    function updateActiveSection() {
        const sections = [
            { id: '#home', selector: '#home' },
            { id: '#about', selector: '#about' },
            { id: '#dates', selector: '#dates' },
            { id: '#papers', selector: '#papers' },
            { id: '#advisory', selector: '#advisory' },
            { id: '#committee', selector: '#committee' },
            { id: '#contact', selector: '#contact' }
        ];

        const scrollPosition = window.scrollY + 100; // Offset for better detection
        
        let activeSection = null;
        
        sections.forEach(section => {
            const element = document.querySelector(section.selector);
            if (element) {
                const rect = element.getBoundingClientRect();
                const elementTop = rect.top + window.scrollY;
                const elementBottom = elementTop + rect.height;
                
                if (scrollPosition >= elementTop && scrollPosition < elementBottom) {
                    activeSection = section.id;
                }
            }
        });

        // Update desktop nav links
        if (desktopNavLinks) {
            desktopNavLinks.querySelectorAll('a').forEach(link => {
                const href = link.getAttribute('href');
                if (href && href.startsWith('#')) {
                    const sectionId = href;
                    if (sectionId === activeSection) {
                        link.classList.add('nav-link-active');
                    } else {
                        link.classList.remove('nav-link-active');
                    }
                }
            });
        }

        // Update mobile menu items
        mobileMenuItems.forEach(item => {
            const href = item.getAttribute('href');
            if (href && href.startsWith('#')) {
                const sectionId = href;
                if (sectionId === activeSection) {
                    item.classList.add('mobile-menu-item-active');
                } else {
                    item.classList.remove('mobile-menu-item-active');
                }
            }
        });
    }

    // Throttled scroll handler for active section
    let sectionTicking = false;
    function onScrollForSection() {
        if (!sectionTicking) {
            requestAnimationFrame(updateActiveSection);
            sectionTicking = true;
            setTimeout(() => { sectionTicking = false; }, 100);
        }
    }

    // Initialize
    window.addEventListener('scroll', onScroll);
    window.addEventListener('scroll', onScrollForSection);
    updateNavbarState(); // Initial state
    updateActiveSection(); // Initial active section

    // Handle smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            const target = document.querySelector(href);
            
            if (target) {
                e.preventDefault();
                const offsetTop = target.offsetTop - 80; // Account for navbar height
                
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
                
                // Close mobile menu if open
                const mobileMenu = document.getElementById('mobile-menu');
                if (mobileMenu && mobileMenu.classList.contains('open')) {
                    const btn = document.getElementById('hamburger-btn');
                    const icon = document.getElementById('hamburger-icon');
                    
                    mobileMenu.classList.remove('open', 'hidden');
                    mobileMenu.classList.add('hidden');
                    mobileMenu.setAttribute('aria-hidden', 'true');
                    btn.setAttribute('aria-expanded', 'false');
                    if (icon) icon.textContent = 'menu';
                }
            }
        });
    });
})();

// Scroll-based animations for major sections
(function () {
    const sections = [
        '#about',
        '#venue',
        '#sponsor',
        '#speakers',
        '#advisory',
        '#committee'
    ];

    // If IntersectionObserver isn't supported, just show everything
    if (!('IntersectionObserver' in window)) {
        sections.forEach(selector => {
            const element = document.querySelector(selector);
            if (element) {
                element.classList.add('scroll-animate', 'is-visible');
            }
        });
        return;
    }

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                // Stop observing after animation triggers once
                observer.unobserve(entry.target);
            }
        });
    }, { 
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px' // Trigger slightly before element comes into view
    });

    sections.forEach(selector => {
        const element = document.querySelector(selector);
        if (element) {
            // Add fade-up class for sections that should slide up
            if (selector === '#about' || selector === '#venue' || selector === '#sponsor') {
                element.classList.add('fade-up');
            }
            
            observer.observe(element);
        }
    });
})();
