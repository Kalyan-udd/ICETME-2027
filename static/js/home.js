// Simple script for mobile menu toggle
document.querySelector('button.lg\\:hidden').addEventListener('click', function() {
    const menu = document.querySelector('.lg\\:flex');
    menu.classList.toggle('hidden');
    menu.classList.toggle('flex');
    menu.classList.toggle('flex-col');
    menu.classList.toggle('absolute');
    menu.classList.toggle('top-full');
    menu.classList.toggle('left-0');
    menu.classList.toggle('w-full');
    menu.classList.toggle('bg-white');
    menu.classList.toggle('p-6');
    menu.classList.toggle('shadow-xl');
    menu.classList.toggle('dark:bg-slate-900');
});
