import os

def list_desktop_files():
    desktop_path = os.path.join(os.path.expanduser("~"), "Skrivebord")
    if os.path.exists(desktop_path):
        files = os.listdir(desktop_path)
        print(*files, sep="\n")
    else:
        print(f"Desktop directory does not exist: {desktop_path}")

if __name__ == "__main__":
    list_desktop_files()
