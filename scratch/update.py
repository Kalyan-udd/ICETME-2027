import re
import os

with open(r'c:\Users\SOMRAJ\OneDrive\Desktop\ICETME-2027-repo\templates\home.html', 'r', encoding='utf-8') as f:
    content = f.read()

def sanitize_name(name):
    # remove "Prof. " or "Dr. " or "Mr. " prefix
    name = re.sub(r'^(Prof\.|Dr\.|Mr\.)\s*', '', name).strip()
    return re.sub(r'[\s.]+', '_', name).lower()

# 1. Update International Board
start_int = content.find('<!-- International -->')
end_int = content.find('<!-- National -->')
int_section = content[start_int:end_int]

cards = re.split(r'(<div class="bg-surface-container-lowest.*?)(?=<div class="bg-surface-container-lowest|</div>\s+</div>\s+<!-- National)', int_section, flags=re.DOTALL)
new_cards = []
for c in cards:
    if c.startswith('<div class="bg-surface-container-lowest'):
        name_search = re.search(r'<h4[^>]*>(.*?)</h4>', c)
        if name_search:
            full_name = name_search.group(1)
            bname = sanitize_name(full_name)
            c = re.sub(r'src="[^"]*"', f'src="static/images/international_advisory/{bname}.jpeg"', c)
            c = re.sub(r'alt="[^"]*"', f'alt="{full_name}"', c)
    new_cards.append(c)

new_int_section = "".join(new_cards)

# 2. Update National Board
start_nat = content.find('<!-- National -->')
end_nat = content.find('<!-- Important Dates -->')
nat_section = content[start_nat:end_nat]

cards_nat = re.split(r'(<div class="bg-surface-container-low p-5 rounded-2xl border border-outline-variant/10 shadow-sm card-hover">.*?</div>)', nat_section, flags=re.DOTALL)
new_cards_nat = []
for c in cards_nat:
    if c.startswith('<div class="bg-surface-container-low'):
        name_search = re.search(r'<h4[^>]*>(.*?)</h4>', c)
        if name_search:
            full_name = name_search.group(1)
            bname = sanitize_name(full_name)
            # Add the image wrap structure right before <h4> if not already present
            if '<img' not in c:
                img_block = f"""
                    <div class="w-16 h-16 mb-4 mx-auto relative group">
                        <div class="absolute inset-0 bg-primary/5 rounded-full group-hover:bg-primary/10 transition-colors"></div>
                        <img src="static/images/national_advisory/{bname}.jpeg" alt="{full_name}" onerror="this.onerror=null; this.src='static/images/placeholder.png';" class="relative w-full h-full object-cover rounded-full shadow-sm">
                    </div>"""
                # insert it before <h4>
                c = re.sub(r'(<h4)', img_block + r'\n                    \1', c, count=1)
                
                # If we do this, we should add text-center inline or something? "DO NOT modify CSS classes" -> "card flex flex-col item-center text-center". 
                # Let's ensure it aligns nicely without modifying card css class. I've added mx-auto to center the image. And mb-4.

    new_cards_nat.append(c)

new_nat_section = "".join(new_cards_nat)

final_content = content[:start_int] + new_int_section + new_nat_section + content[end_nat:]

with open(r'c:\Users\SOMRAJ\OneDrive\Desktop\ICETME-2027-repo\templates\home.html', 'w', encoding='utf-8') as f:
    f.write(final_content)

print("done")
