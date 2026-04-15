import os
import re

html_path = r'c:\Users\SOMRAJ\OneDrive\Desktop\ICETME-2027-repo\templates\home.html'
images_dir = r'c:\Users\SOMRAJ\OneDrive\Desktop\ICETME-2027-repo\static\images'

# 1. Gather all existing images
image_map = {}
for root, _, files in os.walk(images_dir):
    for f in files:
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            rel_path = os.path.relpath(os.path.join(root, f), images_dir).replace('\\', '/')
            base_name, _ = os.path.splitext(f)
            image_map[base_name.lower()] = f'/static/images/{rel_path}'

def sanitize_name(name):
    name = re.sub(r'^(Prof\.|Dr\.|Mr\.)\s*', '', name).strip()
    return re.sub(r'[\s.]+', '_', name).lower()

def generate_speaker_card(name_line):
    # E.g. "Prof. A. C. Benim . Dusseldorf University of Applied Sciences, Germany"
    if '–' in name_line:
        name_part, affil_part = name_line.split('–', 1)
    elif '-' in name_line:
        name_part, affil_part = name_line.split('-', 1)
    else:
        name_part = name_line
        affil_part = ""
        
    name = name_part.strip()
    affiliation = affil_part.strip()
    
    bname = sanitize_name(name)
    
    # Resolve image path
    if bname in image_map:
        img_src = image_map[bname]
    else:
        # Default placeholder logic + easy replacement
        img_src = f"/static/images/speakers/{bname}.jpeg"
        
    return f"""                <div class="bg-surface-container-lowest p-6 rounded-3xl border border-outline-variant/20 shadow-sm card-hover flex flex-col items-center text-center">
                    <div class="w-24 h-24 mb-4 relative group">
                        <div class="absolute inset-0 bg-primary/10 rounded-full group-hover:bg-primary/20 transition-colors"></div>
                        <img src="{img_src}" alt="{name}" onerror="this.onerror=null; this.src='/static/images/placeholder.png';" class="relative w-full h-full object-cover rounded-full border-2 border-primary/20 shadow-md">
                    </div>
                    <h4 class="font-headline font-bold text-lg text-on-surface mb-2">{name}</h4>
                    <p class="text-sm text-primary font-semibold">{affiliation}</p>
                </div>"""

plenary_raw = [
    "Prof. A. C. Benim - Düsseldorf University of Applied Sciences, Germany",
    "Prof. Bidyut Baran Saha - Kyushu University, Japan",
    "Prof. J. Paulo Davim - University of Aveiro, Portugal",
    "Prof. Kalyanmoy Deb - Michigan State University, USA",
    "Prof. Xiaolin Wang - University of Tasmania, Australia"
]

keynote_raw = [
    "Prof. A Senthil Kumar - National University of Singapore",
    "Prof. Amitava De - IIT Bombay",
    "Prof. G. K. Ananthasuresh - IISc Bangalore",
    "Prof. Kaushik Pal - IIT Roorkee",
    "Prof. Rajat Gupta - Veltech University",
    "Dr. S. P. Aggarwal - Director, NESAC (ISRO)",
    "Prof. Sreedhara Sheshadri - IIT Bombay",
    "Prof. Subrata Sarkar - IIT Kanpur",
    "Prof. Sudarshan Kumar - IIT Bombay",
    "Prof. Sudarshan Ghosh - IIT Delhi"
]

session_raw = [
    "Prof. Achinto Mukhopadhay - Jadavpur University",
    "Prof. Amaresh Dalal - IIT Guwahati",
    "Prof. Anirban Mitra - Jadavpur University",
    "Prof. Apurba Layek - NIT Durgapur",
    "Prof. Bijan Kumar Madal - IIEST Shibpur",
    "Prof. Dibakar Sen - IISc Bangalore",
    "Prof. Pankaj Biswas - IIT Guwahati",
    "Prof. Prasanto Sahoo - Jadavpur University",
    "Prof. R. K. Garg - NIT Jalandhar",
    "Prof. Rajesh Ghosh - IIT Mandi",
    "Prof. U. S. Dixit - IIT Guwahati",
    "Dr. Sudip Dey - NIT Silchar"
]

def make_grid(speakers):
    return "\n".join(generate_speaker_card(s) for s in speakers)

speakers_html = f"""
<!-- Speakers Section -->
<section id="speakers" class="py-32 bg-surface-container-low">
    <div class="container mx-auto px-6 max-w-7xl">
        <div class="text-center mb-24">
            <h2 class="font-headline text-4xl md:text-6xl font-extrabold text-on-background tracking-tight mb-6">Distinguished <span class="gradient-text">Speakers</span></h2>
            <p class="text-xl text-on-surface-variant max-w-2xl mx-auto">Hear from leading experts and academicians across the globe.</p>
        </div>

        <!-- Plenary Speakers -->
        <div class="mb-24">
            <div class="flex items-center gap-4 mb-12">
                <span class="material-symbols-outlined text-4xl text-primary">campaign</span>
                <h3 class="font-headline text-3xl font-bold text-on-background">Plenary Speakers</h3>
                <div class="h-px bg-outline-variant/30 flex-grow ml-4"></div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
{make_grid(plenary_raw)}
            </div>
        </div>

        <!-- Keynote Speakers -->
        <div class="mb-24">
            <div class="flex items-center gap-4 mb-12">
                <span class="material-symbols-outlined text-4xl text-primary">mic</span>
                <h3 class="font-headline text-3xl font-bold text-on-background">Keynote Speakers</h3>
                <div class="h-px bg-outline-variant/30 flex-grow ml-4"></div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
{make_grid(keynote_raw)}
            </div>
        </div>

        <!-- Session Speakers -->
        <div>
            <div class="flex items-center gap-4 mb-12">
                <span class="material-symbols-outlined text-4xl text-primary">record_voice_over</span>
                <h3 class="font-headline text-3xl font-bold text-on-background">Session Speakers</h3>
                <div class="h-px bg-outline-variant/30 flex-grow ml-4"></div>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
{make_grid(session_raw)}
            </div>
        </div>
    </div>
</section>
"""

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Determine where to insert it. Before "<!-- Important Dates -->"
marker = "<!-- Important Dates -->"
if marker in html:
    new_html = html.replace(marker, speakers_html + "\n" + marker)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Injected successfully.")
else:
    print("Marker not found!")
