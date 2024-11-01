import os
from pathlib import Path

desktop_path = Path(os.path.expanduser("~")) / "OneDrive/Skrivebord"

def list_desktop_files():
    if os.path.exists(desktop_path):
        files = os.listdir(desktop_path)
        return files
    else:
        print(f"Desktop directory does not exist: {desktop_path}")

def move_files():
    files = list_desktop_files()

    for file in files:
        extension = Path(file).suffix
        print(extension)
        folder = desktop_path / extension

        if not folder.exists():
            folder.mkdir()
        (desktop_path / file).rename(folder / file)

if __name__ == "__main__":
    move_files()
