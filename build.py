#!/usr/bin/env python3
"""
Build script for HOBBY RADSPORT CC static site.
Generates HTML grid items from images in img/ folder.
"""

from pathlib import Path

# Configuration
REPO_ROOT = Path(__file__).parent
IMG_DIR = REPO_ROOT / "img"
INDEX_FILE = REPO_ROOT / "index.html"
TEMPLATE_FILE = REPO_ROOT / "index.template.html"

# Supported image extensions
IMAGE_EXTENSIONS = {".gif", ".png", ".jpg", ".jpeg", ".svg"}

# Marker comments for injection
START_MARKER = "<!-- STICKER_GRID_START -->"
END_MARKER = "<!-- STICKER_GRID_END -->"


def get_display_name(filename: str) -> str:
    """Convert filename to display name.

    Examples:
        '001_aebbelwoi.gif' -> 'AEBBELWOI'
        '002_s_wurst.png' -> 'S WURST'
        '003_tourer_pace_black.png' -> 'TOURER PACE BLACK'
    """
    stem = Path(filename).stem
    # Strip "001_" prefix (first 4 characters)
    if len(stem) > 4 and stem[3] == "_":
        stem = stem[4:]
    return stem.replace("_", " ").upper()


def get_images() -> list[Path]:
    """Get all images from img/ folder, excluding subdirectories."""
    images = []
    for item in IMG_DIR.iterdir():
        if item.is_file() and item.suffix.lower() in IMAGE_EXTENSIONS:
            if not item.name.startswith("."):
                images.append(item)

    return sorted(images, key=lambda p: p.name.lower())


def generate_grid_item(image: Path) -> str:
    """Generate HTML for a single grid item."""
    display_name = get_display_name(image.name)
    relative_path = f"img/{image.name}"

    return f'''      <article class="sticker-item">
        <img src="{relative_path}" alt="{display_name}">
      </article>'''


def build():
    """Main build function."""
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = f.read()

    if START_MARKER not in template or END_MARKER not in template:
        raise ValueError(f"Template missing markers: {START_MARKER} and/or {END_MARKER}")

    images = get_images()
    grid_html = "\n\n".join(generate_grid_item(img) for img in images)

    start_idx = template.index(START_MARKER) + len(START_MARKER)
    end_idx = template.index(END_MARKER)

    output = template[:start_idx] + "\n\n" + grid_html + "\n\n" + template[end_idx:]

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"Built index.html with {len(images)} images:")
    for img in images:
        print(f"  - {img.name}")


if __name__ == "__main__":
    build()
