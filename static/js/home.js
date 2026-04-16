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
