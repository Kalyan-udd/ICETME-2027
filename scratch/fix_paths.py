import re

file_path = r'c:\Users\SOMRAJ\OneDrive\Desktop\ICETME-2027-repo\templates\home.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace src="static/images/international_advisory/
content = content.replace('src="static/images/international_advisory/', 'src="/static/images/international_advisory/')

# Replace src="static/images/national_advisory/
content = content.replace('src="static/images/national_advisory/', 'src="/static/images/national_advisory/')

# Replace src='static/images/placeholder.png' inside onerror
content = content.replace("this.src='static/images/placeholder.png'", "this.src='/static/images/placeholder.png'")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Replaced paths successfully.')
