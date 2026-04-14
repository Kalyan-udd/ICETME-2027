import re

css_path = r'c:\Users\SOMRAJ\OneDrive\Desktop\ICETME-2027-repo\static\css\home.css'

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the nav-link section entirely
nav_link_replacement = """
.navbar-glass {
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(0, 31, 100, 0.05);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
}

.nav-link {
    position: relative;
    padding-bottom: 4px;
    color: #434656;
    transition: color 0.3s ease;
}
.nav-link::after {
    content: '';
    position: absolute;
    width: 0;
    height: 2px;
    bottom: -2px;
    left: 50%;
    background: linear-gradient(90deg, #003ec7, #0052ff);
    transition: all 0.3s ease;
    transform: translateX(-50%);
    border-radius: 2px;
}
.nav-link:hover, .nav-link.active {
    color: #003ec7;
}
.nav-link:hover::after, .nav-link.active::after {
    width: 100%;
}
"""

css = re.sub(r'\.nav-link\s*{.*?(?=\.card-hover)', nav_link_replacement, css, flags=re.DOTALL)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS updated!")

html_path = r'c:\Users\SOMRAJ\OneDrive\Desktop\ICETME-2027-repo\templates\home.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the nav opening tag
html = re.sub(
    r'<nav class="glass-card rounded-full sticky top-6 z-50 max-w-7xl mx-auto flex justify-between items-center w-\[95%\] px-8 py-4 transition-all duration-300">',
    r'<nav class="navbar-glass fixed top-0 left-0 w-full z-[100] flex justify-between items-center px-6 lg:px-12 py-4 transition-all duration-300">',
    html
)

# Replace the hero padding
html = re.sub(
    r'<header id="home" class="relative min-h-\[85vh\] flex items-center justify-center pt-8 pb-16 overflow-hidden hero-mesh">',
    r'<header id="home" class="relative min-h-[85vh] flex items-center justify-center pt-28 pb-16 overflow-hidden hero-mesh">',
    html
)

# In the desktop menu, removing the Tailwind text colors to let CSS handle it
menu_regex = r'<a class="nav-link font-headline tracking-tight text-sm font-semibold uppercase text-on-background hover:text-primary transition-colors"'
new_menu_class = r'<a class="nav-link font-headline tracking-tight text-sm font-semibold uppercase transition-colors"'
html = html.replace(menu_regex, new_menu_class)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML updated!")
