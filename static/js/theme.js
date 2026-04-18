// Dark Mode Toggle Functionality
(function () {
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const darkModeIcon = document.getElementById('dark-mode-icon');
    const body = document.body;

    if (!darkModeToggle || !darkModeIcon) return;

    // Check for saved theme preference or default to light mode
    const savedTheme = localStorage.getItem('darkMode');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    // Set initial theme
    if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
        body.classList.add('dark-mode');
        darkModeIcon.textContent = 'dark_mode';
    } else {
        darkModeIcon.textContent = 'light_mode';
    }

    // Toggle dark mode
    function toggleDarkMode() {
        const isDarkMode = body.classList.toggle('dark-mode');
        
        // Update icon
        darkModeIcon.textContent = isDarkMode ? 'dark_mode' : 'light_mode';
        
        // Add rotation animation
        darkModeIcon.style.transform = 'rotate(360deg)';
        setTimeout(() => {
            darkModeIcon.style.transform = 'rotate(0deg)';
        }, 300);
        
        // Save preference
        localStorage.setItem('darkMode', isDarkMode ? 'dark' : 'light');
        
        // Dispatch custom event for other components
        window.dispatchEvent(new CustomEvent('themeChange', { 
            detail: { isDarkMode } 
        }));
    }

    // Event listeners
    darkModeToggle.addEventListener('click', toggleDarkMode);

    // Listen for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!localStorage.getItem('darkMode')) {
            if (e.matches) {
                body.classList.add('dark-mode');
                darkModeIcon.textContent = 'dark_mode';
            } else {
                body.classList.remove('dark-mode');
                darkModeIcon.textContent = 'light_mode';
            }
        }
    });

    // Keyboard support
    darkModeToggle.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            toggleDarkMode();
        }
    });
})();
