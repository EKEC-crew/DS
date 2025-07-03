import os

# 생성 대상 디렉토리 목록
TARGET_DIRS = [
    "icons",
    "logos",
    os.path.join("filters", "category"),
    os.path.join("filters", "activity"),
    os.path.join("filters", "style"),
    os.path.join("filters", "gray"),
]


def generate_readme_for_folder(folder_path):
    svg_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".svg")])
    readme_path = os.path.join(folder_path, "README.md")

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("# SVG Icon List\n\n")
        f.write("This folder contains the following SVG icon files with previews:\n\n")
        for svg in svg_files:
            f.write(f"### {svg}\n\n")
            f.write(f'<img src="./{svg}" alt="{svg}" width="48" height="48" />\n\n')

    print(f"✅ README created: {readme_path} ({len(svg_files)} icons)")


# 실행
if __name__ == "__main__":
    for folder in TARGET_DIRS:
        if os.path.exists(folder):
            generate_readme_for_folder(folder)
        else:
            print(f"⚠️ Folder not found: {folder}")
