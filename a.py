from pathlib import Path
import shutil
import sys

SCRIPT_PATH = Path(__file__).resolve()
PROJECT_ROOT = SCRIPT_PATH.parent

ASSETS_DIR = PROJECT_ROOT / "assets"
IMAGES_DIR = PROJECT_ROOT / "Images"
LOGOS_DIR = PROJECT_ROOT / "Logos"

MAPPINGS = [
    (LOGOS_DIR / "Horizontal_Black_PNG.png", ASSETS_DIR / "logo-dark.png"),
    (LOGOS_DIR / "Horizontal_White_WO.png", ASSETS_DIR / "logo-white.png"),
    (LOGOS_DIR / "SYSICON.ico", ASSETS_DIR / "favicon.ico"),

    (IMAGES_DIR / "Render_Prime.png", ASSETS_DIR / "hero-powerhub-render.png"),
    (IMAGES_DIR / "Render_Prime.png", ASSETS_DIR / "powerhub-core.png"),
    (IMAGES_DIR / "Render_Camo (1).jpeg", ASSETS_DIR / "powerhub-mini.png"),
    (IMAGES_DIR / "Render_Camo (3).jpeg", ASSETS_DIR / "powerhub-pro.png"),
    (IMAGES_DIR / "Render_Camo (6).jpeg", ASSETS_DIR / "powerrack.png"),

    (IMAGES_DIR / "WhatsApp Image 2025-03-16 at 12.48.53.jpeg", ASSETS_DIR / "usecase-school-demo.jpg"),
    (IMAGES_DIR / "Syuniqe_IIMB.jpeg", ASSETS_DIR / "usecase-resort-demo.jpg"),
    (IMAGES_DIR / "RoomSetup_2024-Dec-29_02-14-00PM-000_CustomizedView25799515184.png", ASSETS_DIR / "usecase-field-demo.jpg"),
    (IMAGES_DIR / "Image (1).jpg", ASSETS_DIR / "usecase-pilot-medical.jpg"),
    (IMAGES_DIR / "Image (1).png", ASSETS_DIR / "cta-lifestyle.jpg"),

    (IMAGES_DIR / "DP_Harsh.jpeg", ASSETS_DIR / "team-harsh.jpg"),
    (IMAGES_DIR / "DP_Abhishek.jpeg", ASSETS_DIR / "team-abhishek.jpg"),
    (IMAGES_DIR / "DP_Rohan.jpeg", ASSETS_DIR / "team-rohan.jpg"),

    (IMAGES_DIR / "Syuniqe_IIMB.jpeg", ASSETS_DIR / "about-journey.jpg"),
    (IMAGES_DIR / "Banner_Harsh.jpeg", ASSETS_DIR / "contact-cta.jpg"),
]

def main():
    print("Script path :", SCRIPT_PATH)
    print("Project root:", PROJECT_ROOT)
    print("Images dir  :", IMAGES_DIR)
    print("Logos dir   :", LOGOS_DIR)
    print("Assets dir  :", ASSETS_DIR)

    if not IMAGES_DIR.exists():
        print(f"\nMissing folder: {IMAGES_DIR}")
        return 1
    if not LOGOS_DIR.exists():
        print(f"\nMissing folder: {LOGOS_DIR}")
        return 1

    ASSETS_DIR.mkdir(exist_ok=True)

    missing = []
    copied = []

    for src, dst in MAPPINGS:
        if not src.exists():
            missing.append(src)
            continue
        shutil.copy2(src, dst)
        copied.append((src.name, dst.name))

    print("\nCopied:")
    for src_name, dst_name in copied:
        print(f"  {src_name}  ->  assets\\{dst_name}")

    if missing:
        print("\nMissing files:")
        for m in missing:
            print(f"  {m}")
        return 2

    print("\nAll done.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())