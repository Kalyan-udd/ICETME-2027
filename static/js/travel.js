document.addEventListener("DOMContentLoaded", () => {
        const reveals = document.querySelectorAll('.reveal-up');
        setTimeout(() => {
            reveals.forEach(el => el.classList.add('active'));
        }, 100);
    });