import re

html_path = r'c:\Users\SOMRAJ\OneDrive\Desktop\ICETME-2027-repo\templates\home.html'

students = [
    "Aashika Jaiswal",
    "Ankit Saha",
    "Kalyan Sai Uddagiri",
    "Somraj Deb",
    "Sneha Deb",
    "Prince Rawat"
]

def sanitize_name(name):
    return re.sub(r'[\s.]+', '_', name).lower()

cards = []
for name in students:
    bname = sanitize_name(name)
    img_src = f"/static/images/students/{bname}.jpeg"
    card = f"""                <div class="bg-surface-container-lowest p-6 rounded-3xl border border-outline-variant/20 shadow-sm card-hover flex flex-col items-center text-center">
                    <div class="w-24 h-24 mb-4 relative group">
                        <div class="absolute inset-0 bg-primary/10 rounded-full group-hover:bg-primary/20 transition-colors"></div>
                        <img src="{img_src}" alt="{name}" onerror="this.onerror=null; this.src='/static/images/placeholder.png';" class="relative w-full h-full object-cover rounded-full border-2 border-primary/20 shadow-md">
                    </div>
                    <h4 class="font-headline font-bold text-lg text-on-surface mb-2">{name}</h4>
                    <p class="text-sm text-primary font-semibold">Student Committee</p>
                </div>"""
    cards.append(card)

grid = "\n".join(cards)

section_html = f"""
        <!-- Student Committee -->
        <div class="mt-24">
            <div class="flex items-center gap-4 mb-12">
                <span class="material-symbols-outlined text-4xl text-primary">groups</span>
                <h3 class="font-headline text-3xl font-bold text-on-background">Student Committee</h3>
                <div class="h-px bg-outline-variant/30 flex-grow ml-4"></div>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-6 gap-6">
{grid}
            </div>
        </div>
"""

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# We want to insert it after the Organizing Secretaries, right before the closing of #committee section.
os_marker = '</div>\n        </div>\n    </div>\n</section>'
os_marker_2 = '</div>\n    </div>\n</section>'
# Wait, let's just find the end of Organizing Secretaries block.
# the view_file showed:
# 966:             </div>
# 967:         </div>
# 968:     </div>
# 969: </section>
# 970: 
# 971: <!-- Footer -->
marker_index = html.find('<!-- Footer -->')
# We need to insert our section_html right before "    </div>\n</section>\n\n<!-- Footer -->"
# It's safer to use regex to find the end of #committee section.
m = re.search(r'(</section>\s+<!-- Footer -->)', html)
if m:
    # insert before the closing section tag
    new_html = re.sub(r'(    </div>\n</section>\s+<!-- Footer -->)', section_html + r'\1', html)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Injected successfully.")
else:
    print("Marker not found.")
