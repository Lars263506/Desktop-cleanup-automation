import os
from pathlib import Path

desktop_path = Path(os.path.expanduser("~")) / "OneDrive/Skrivebord"
files_folder = desktop_path / "files"

def list_desktop_files():
    if os.path.exists(desktop_path):
        files = os.listdir(desktop_path)
        return files
    else:
        print(f"Desktop directory does not exist: {desktop_path}")

def move_files():
    files = list_desktop_files()

    if not files_folder.exists():
        files_folder.mkdir()

    for file in files:
        file_path = desktop_path / file
        if file_path.is_file():
            file_path.rename(files_folder / file)


if __name__ == "__main__":
    move_files()
