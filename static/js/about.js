document.addEventListener("DOMContentLoaded", function() {

    // ==========================================
    // 1. STICKY NAV SCROLL BEHAVIOUR
    // ==========================================
    // #nav-wrapper holds the sticky position + width; #main-nav is the pill that gets shadow/bg
    const navWrapper = document.getElementById('nav-wrapper');
    const navPill    = document.getElementById('main-nav');
    if (navWrapper && navPill) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navWrapper.classList.remove('top-6', 'w-[95%]');
                navWrapper.classList.add('top-0', 'w-full');
                navPill.classList.add('shadow-lg', 'bg-white/90', 'rounded-2xl');
                navPill.classList.remove('rounded-full');
            } else {
                navWrapper.classList.add('top-6', 'w-[95%]');
                navWrapper.classList.remove('top-0', 'w-full');
                navPill.classList.remove('shadow-lg', 'bg-white/90', 'rounded-2xl');
                navPill.classList.add('rounded-full');
            }
        });
    }

    // ==========================================
    // 2. SCROLL REVEAL ANIMATOR
    // ==========================================
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.reveal-up').forEach(el => {
        observer.observe(el);
    });

    // ==========================================
    // 3. NITA FADING SLIDESHOW
    // ==========================================
    const nitaSlides = document.querySelectorAll('.nita-slide');

    if (nitaSlides.length > 0) {
        let currentSlide = 0;

        setInterval(() => {
            nitaSlides[currentSlide].classList.remove('opacity-100');
            nitaSlides[currentSlide].classList.add('opacity-0');

            currentSlide = (currentSlide + 1) % nitaSlides.length;

            nitaSlides[currentSlide].classList.remove('opacity-0');
            nitaSlides[currentSlide].classList.add('opacity-100');
        }, 3500);
    }

    // ==========================================
    // 4. TRIPURA FADING SLIDESHOW
    // ==========================================
    const tripuraSlides = document.querySelectorAll('.tripura-slide');

    if (tripuraSlides.length > 0) {
        let currentTripSlide = 0;

        setInterval(() => {
            tripuraSlides[currentTripSlide].classList.remove('opacity-100');
            tripuraSlides[currentTripSlide].classList.add('opacity-0');

            currentTripSlide = (currentTripSlide + 1) % tripuraSlides.length;

            tripuraSlides[currentTripSlide].classList.remove('opacity-0');
            tripuraSlides[currentTripSlide].classList.add('opacity-100');
        }, 4000);
    }

});

