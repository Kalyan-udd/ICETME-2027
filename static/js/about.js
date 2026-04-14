document.addEventListener("DOMContentLoaded", function() {
    
    // ==========================================
    // 1. NAVIGATION CONTROLLER (Menu & Sticky Nav)
    // ==========================================
    const mobileBtn = document.querySelector('button.lg\\:hidden');
    const navMenu = document.querySelector('.hidden.lg\\:flex');

    if (mobileBtn && navMenu) {
        mobileBtn.addEventListener('click', function() {
            navMenu.classList.toggle('hidden');
            navMenu.classList.toggle('flex-col');
            navMenu.classList.toggle('absolute');
            navMenu.classList.toggle('top-24');
            navMenu.classList.toggle('left-0');
            navMenu.classList.toggle('w-full');
            navMenu.classList.toggle('bg-white/95');
            navMenu.classList.toggle('backdrop-blur-xl');
            navMenu.classList.toggle('p-8');
            navMenu.classList.toggle('shadow-2xl');
            navMenu.classList.toggle('rounded-3xl');
            navMenu.classList.toggle('z-50');
        });
    }

    const navbar = document.querySelector('nav');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('shadow-lg', 'bg-white/90');
            navbar.classList.remove('w-[95%]', 'top-6');
            navbar.classList.add('w-full', 'top-0');
        } else {
            navbar.classList.remove('shadow-lg', 'bg-white/90');
            navbar.classList.remove('w-full', 'top-0');
            navbar.classList.add('w-[95%]', 'top-6');
        }
    });

    // ==========================================
    // 2. SCROLL REVEAL ANIMATOR
    // ==========================================
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
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
    // 3. NITA FADING SLIDESHOW (Campus Photos ONLY)
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
    // 4. TRIPURA FADING SLIDESHOW (Tripura & Airport ONLY)
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
