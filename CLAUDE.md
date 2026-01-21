# CLAUDE.md - AI Assistant Guide

## Project Overview

**HOBBY RADSPORT CC** is a static website for a cycling club showcasing a gallery of sticker/logo designs. The site is hosted on GitHub Pages at `hobbyradsport.cc`.

## Repository Structure

```
hobbyrs/
├── CNAME                    # GitHub Pages custom domain config
├── README.md                # Project description
├── build.py                 # Python build script (auto-generates index.html)
├── index.template.html      # HTML template with CSS and layout
├── index.html               # AUTO-GENERATED - do not edit directly
├── hooks/
│   └── pre-commit           # Git hook that runs build.py before commits
└── img/
    ├── *.gif/png/jpg        # Gallery images (numbered prefix + snake_case name)
    ├── excl/                # Excluded images (not displayed on site)
    └── logo/                # Site branding assets
```

## Build System

### How It Works

1. `build.py` scans the `img/` directory for images (.gif, .png, .jpg, .jpeg, .svg)
2. Generates HTML grid items from image filenames
3. Injects content between markers in `index.template.html`:
   - `<!-- STICKER_GRID_START -->`
   - `<!-- STICKER_GRID_END -->`
4. Outputs the complete page to `index.html`

### Running the Build

```bash
python3 build.py
```

### Pre-commit Hook

The `hooks/pre-commit` script automatically:
- Runs `build.py` before each commit
- Stages the regenerated `index.html`
- Aborts commit if build fails

## Development Workflow

### Adding a New Image

1. Add image to `img/` directory with naming format: `NNN_descriptive_name.ext`
   - NNN = three-digit number for ordering (e.g., 011, 012)
   - Use snake_case for the descriptive name
   - The name becomes the alt-text (uppercase, spaces replace underscores)
2. Run `python3 build.py` or commit (pre-commit hook handles it)

### Excluding an Image

Move the image to `img/excl/` to keep it in version control but hide it from the gallery.

### Modifying Layout/Styling

Edit `index.template.html` directly. Changes to CSS, header, or page structure go here.

**Never edit `index.html` directly** - it gets overwritten by the build process.

## Code Conventions

### Image Naming

- Format: `NNN_name.ext` (e.g., `007_tourer_pace_black.png`)
- Numeric prefix controls display order
- Name becomes alt-text: `007_tourer_pace_black.png` → "TOURER PACE BLACK"

### Supported Image Formats

- `.gif`, `.png`, `.jpg`, `.jpeg`, `.svg`

### HTML/CSS

- German language (`lang="de"`)
- Mobile-first responsive design
- CSS Grid with breakpoints: 1 column (mobile), 2 (768px), 3 (1024px), 4 (1400px)
- Embedded CSS in template (no external stylesheets)

## Key Files Reference

| File | Purpose | Editable? |
|------|---------|-----------|
| `index.template.html` | HTML/CSS template | Yes |
| `build.py` | Build script | Yes |
| `index.html` | Generated output | No (auto-generated) |
| `CNAME` | Domain config | Rarely |
| `hooks/pre-commit` | Git automation | If needed |

## Dependencies

- **Python 3** with standard library only (uses `pathlib`)
- No external packages required

## Git Workflow

### Branches

- `main` is the production branch (deployed to GitHub Pages)
- Feature branches prefixed with `claude/` for AI-assisted development

### Commits

Pre-commit hook ensures `index.html` stays in sync with images automatically.

## Contact

Site email: `mail@hobbyradsport.cc`

## Quick Commands

```bash
# Regenerate the site
python3 build.py

# Add new image and rebuild
cp new_image.png img/011_new_design.png
python3 build.py

# Exclude an image
mv img/003_old_design.svg img/excl/

# Check current images
ls img/*.{gif,png,jpg,jpeg,svg} 2>/dev/null
```
