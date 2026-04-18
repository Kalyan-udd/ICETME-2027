with open("static/css/home.css", "r", encoding="utf-8") as f:
    lines = f.readlines()

theme_css = lines[:337] + lines[373:387]
home_css = lines[337:373] + lines[387:]

with open("static/css/theme.css", "w", encoding="utf-8") as f:
    f.writelines(theme_css)
    f.write("\n/* Support for mobile menu in other pages */\n")
    f.write("body.dark-mode #mobile-menu {\n")
    f.write("    background: rgba(26, 26, 26, 0.95) !important;\n")
    f.write("    border: 1px solid rgba(255, 255, 255, 0.1) !important;\n")
    f.write("}\n")

with open("static/css/home.css", "w", encoding="utf-8") as f:
    f.writelines(home_css)

with open("static/js/home.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

theme_js = lines[:66]
home_js = lines[66:]

with open("static/js/theme.js", "w", encoding="utf-8") as f:
    f.writelines(theme_js)

with open("static/js/home.js", "w", encoding="utf-8") as f:
    f.writelines(home_js)
