import re

with open("templates/home.html", "r", encoding="utf-8") as f:
    html = f.read()

original_len = len(html)
print(f"Original file length: {original_len} chars")

# ============================================================
# 1. ORGANISING SECRETARIES — Replace entire grid block
# ============================================================
org_old = (
    '    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-6 gap-6">\n'
    '        \n'
    '        <div class="bg-surface-container-lowest p-6 rounded-3xl border border-outline-variant/20 shadow-sm card-hover flex flex-col items-center text-center">\n'
    '            <h4 class="font-headline font-bold text-[15px] text-on-surface leading-tight">Prof. Arindam Majumder</h4>\n'
    '            <p class="text-[13px] text-on-surface-variant mt-1">Mechanical Engineering Department</p>\n'
    '            <p class="text-[13px] text-on-surface-variant">NIT Agartala</p>\n'
    '        </div>\n'
)

if org_old in html:
    print("Found Org Secretaries grid start — replacing full section...")
else:
    print("WARNING: Org Secretaries grid start NOT found. Checking for CRLF...")
    org_old = org_old.replace('\n', '\r\n')
    if org_old in html:
        print("  Found with CRLF. Will use CRLF versions.")
        crlf = True
    else:
        print("  ERROR: Still not found!")
        crlf = False

def make_org_card(name, dept="Mechanical Engineering Department, NIT Agartala"):
    return (
        f'        <div class="bg-surface-container-lowest p-6 rounded-3xl border border-outline-variant/20 shadow-sm card-hover flex flex-col justify-center items-center text-center">\n'
        f'            <h4 class="font-headline font-bold text-base text-on-surface mb-1">{name}</h4>\n'
        f'            <p class="text-[13px] font-semibold text-primary">{dept}</p>\n'
        f'        </div>\n'
    )

org_members = [
    "Prof. Ajoy Kumar Das",
    "Prof. Arindam Majumder",
    "Prof. Dipak Chandra Das",
    "Prof. Madhujit Deb",
    "Prof. Paramvir Singh",
    "Prof. Ranjan Das",
    "Prof. Ravivarman R",
    "Prof. Sagnik Pal",
    "Prof. Swapan Bhaumik",
]

org_new_cards = ''.join(make_org_card(m) for m in org_members)

org_new_grid = (
    '    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 gap-6">\n\n'
    + org_new_cards
    + '    </div>\n'
)

# Find the full old grid (from grid div to closing </div> before </div> of outer mt-16 div)
# We'll use regex to capture from the grid opening to its closing tag
pattern_org = r'    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-6 gap-6">.*?    </div>\n</div>'
match_org = re.search(pattern_org, html, re.DOTALL)
if match_org:
    old_block = match_org.group(0)
    # preserve the outer </div> that closes mt-16 div
    new_block = org_new_grid + '</div>'
    html = html.replace(old_block, new_block, 1)
    print("Org Secretaries section replaced successfully.")
else:
    print("ERROR: Could not find Org Secretaries grid block via regex!")

# ============================================================
# 2. STUDENT COMMITTEE — Replace grid block
# ============================================================
def make_student_card(name, dept="Mechanical Engineering Department, NIT Agartala"):
    return (
        f'                <div class="bg-surface-container-lowest p-6 rounded-3xl border border-outline-variant/20 shadow-sm card-hover flex flex-col justify-center items-center text-center">\n'
        f'                    <h4 class="font-headline font-bold text-base text-on-surface mb-1">{name}</h4>\n'
        f'                    <p class="text-[13px] font-semibold text-primary">{dept}</p>\n'
        f'                </div>\n'
    )

student_members = [
    "Aashika Jaiswal",
    "Ankit Saha",
    "Kalyan Sai Uddagiri",
    "Somraj Deb",
    "Sneha Deb",
    "Prince Rawat",
]

student_cards = ''.join(make_student_card(m) for m in student_members)

student_new_grid = (
    '            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 gap-6">\n'
    + student_cards
    + '            </div>\n'
)

pattern_student = r'            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-6 gap-6">.*?            </div>'
match_student = re.search(pattern_student, html, re.DOTALL)
if match_student:
    html = html.replace(match_student.group(0), student_new_grid.rstrip('\n'), 1)
    print("Student Committee section replaced successfully.")
else:
    print("ERROR: Could not find Student Committee grid block!")

# ============================================================
# 3. INTERNATIONAL ADVISORY BOARD — Remove photo containers
# ============================================================
# Remove: <div class="w-24 h-24 mb-4 relative"> ... </div>  (the photo circle)
# The pattern is a div with class containing "w-24 h-24"
before_int = html.count('w-24 h-24 mb-4 relative')
html = re.sub(
    r'\s*<div class="w-24 h-24 mb-4 relative">\s*<div[^>]*></div>\s*<img[^>]+>\s*</div>',
    '',
    html,
    flags=re.DOTALL
)
after_int = html.count('w-24 h-24 mb-4 relative')
print(f"International photo divs removed: {before_int - after_int} (of {before_int})")

# ============================================================
# 4. NATIONAL ADVISORY BOARD — Remove photo containers + 3 members
# ============================================================
before_nat = html.count('w-16 h-16 mb-4 mx-auto relative group')
html = re.sub(
    r'\s*<div class="w-16 h-16 mb-4 mx-auto relative group">\s*<div[^>]*></div>\s*<img[^>]+>\s*</div>',
    '',
    html,
    flags=re.DOTALL
)
after_nat = html.count('w-16 h-16 mb-4 mx-auto relative group')
print(f"National photo divs removed: {before_nat - after_nat} (of {before_nat})")

# Remove 3 members from National Advisory Board
# Each card looks like: <div class="bg-surface-container-low p-5 ..."> \n ...<h4>Name</h4><p>...</p>\n </div>
remove_names = ["Prof. Ajoy Kumar Das", "Prof. Ranjan Das", "Prof. Swapan Bhaumik"]
for name in remove_names:
    pattern = r'<div class="bg-surface-container-low p-5 rounded-2xl border border-outline-variant/10 shadow-sm card-hover">\s*<h4[^>]*>' + re.escape(name) + r'</h4><p[^>]*>[^<]*</p>\s*</div>\s*'
    before_count = len(re.findall(pattern, html, re.DOTALL))
    html = re.sub(pattern, '', html, flags=re.DOTALL)
    after_count = len(re.findall(pattern, html, re.DOTALL))
    print(f"Removed '{name}': {before_count} occurrences found and removed")

# Add text-center to national advisory board cards (they didn't have it before)
html = html.replace(
    'class="bg-surface-container-low p-5 rounded-2xl border border-outline-variant/10 shadow-sm card-hover"',
    'class="bg-surface-container-low p-5 rounded-2xl border border-outline-variant/10 shadow-sm card-hover text-center"'
)

print(f"\nFinal file length: {len(html)} chars (delta: {len(html) - original_len})")

with open("templates/home.html", "w", encoding="utf-8") as f:
    f.write(html)

print("File written successfully!")
