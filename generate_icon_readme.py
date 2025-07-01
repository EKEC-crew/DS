import os

ICON_DIR = "icons"
README_PATH = os.path.join(ICON_DIR, "README.md")

# 아이콘 리스트 수집
svg_files = sorted([f for f in os.listdir(ICON_DIR) if f.endswith(".svg")])

# README.md 내용 구성
with open(README_PATH, "w", encoding="utf-8") as f:
    f.write("# SVG Icon List\n\n")
    f.write("This folder contains the following SVG icon files with previews:\n\n")

    for file in svg_files:
        f.write(f"### {file}\n\n")
        f.write(f'<img src="./{file}" alt="{file}" width="48" height="48" />\n\n')

print(f"✅ README.md updated with {len(svg_files)} icon previews.")
