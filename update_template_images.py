import os, re

# Read current generate_templates.py
with open(r"c:\Users\URVASHI BHARTI\OneDrive\Desktop\zoop\generate_templates.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Fix template image definitions for Baby Shower (33-42), Birthday (43-50), Housewarming (51-55)
# In templates 33 to 42:
code = re.sub(
    r'("category_key":\s*"babyshower",.*?"hero_img":\s*")[^"]+(".*?"cover_img":\s*")[^"]+(".*?"c1_img":\s*")[^"]+(".*?"c2_img":\s*")[^"]+(")',
    r'\1../assets/img/baby_hero.svg\2../assets/img/baby_cover.svg\3../assets/img/baby_hero.svg\4../assets/img/baby_cover.svg\5',
    code, flags=re.DOTALL
)

# In templates 43 to 50:
code = re.sub(
    r'("category_key":\s*"birthday",.*?"hero_img":\s*")[^"]+(".*?"cover_img":\s*")[^"]+(".*?"c1_img":\s*")[^"]+(".*?"c2_img":\s*")[^"]+(")',
    r'\1../assets/img/bday_hero.svg\2../assets/img/bday_cover.svg\3../assets/img/bday_cover.svg\4../assets/img/bday_hero.svg\5',
    code, flags=re.DOTALL
)

# In templates 51 to 55:
code = re.sub(
    r'("category_key":\s*"housewarming",.*?"hero_img":\s*")[^"]+(".*?"cover_img":\s*")[^"]+(".*?"c1_img":\s*")[^"]+(".*?"c2_img":\s*")[^"]+(")',
    r'\1../assets/img/house_hero.svg\2../assets/img/house_cover.svg\3../assets/img/house_family.svg\4../assets/img/house_residence.svg\5',
    code, flags=re.DOTALL
)

with open(r"c:\Users\URVASHI BHARTI\OneDrive\Desktop\zoop\generate_templates.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Template data images updated in generate_templates.py!")
