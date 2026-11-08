
import os
import shutil
import re
import subprocess
import urllib.request
from pathlib import Path
from urllib.parse import urlparse, unquote

# ==========================================
# VIDEOVAULT CMD
# ==========================================

BASE_DIR = Path(__file__).resolve().parent


def find_ytdlp():
    """Locate yt-dlp.exe next to this script (also accepts names like yt-dlp_1.exe),
    then fall back to yt-dlp on the system PATH."""
    exact = BASE_DIR / "yt-dlp.exe"
    if exact.is_file():
        return exact

    matches = sorted(BASE_DIR.glob("yt-dlp*.exe"))
    if matches:
        return matches[0]

    found = shutil.which("yt-dlp")
    return Path(found) if found else exact


YTDLP = find_ytdlp()
DOWNLOADS = BASE_DIR / "downloads"
HISTORY = BASE_DIR / "history.txt"

DOWNLOADS.mkdir(parents=True, exist_ok=True)


# ==========================================
# DISPLAY
# ==========================================

def banner():
    os.system("cls")
    print("=" * 55)
    print("                 VIDEOVAULT CMD")
    print("          AUTHORIZED MEDIA DOWNLOADER")
    print("=" * 55)
    print()


def pause():
    input("\nPress ENTER to continue...")


# ==========================================
# URL ANALYSIS
# ==========================================

def analyze(url):
    try:
        parsed = urlparse(url)

        if parsed.scheme != "https" or not parsed.hostname:
            return "INVALID", "Enter a valid HTTPS URL."

        if parsed.username or parsed.password:
            return "INVALID", "URLs containing credentials are not accepted."

        path = parsed.path.lower()

        if path.endswith(".vtt"):
            return "SUBTITLE", "VTT subtitle file detected."

        if path.endswith(".ts"):
            return "VIDEO SEGMENT", "This is an individual transport-stream segment."

        if path.endswith(".m3u8"):
            return "MEDIA PLAYLIST", "This is an HLS media playlist."

        if path.endswith(".mp4"):
            return "DIRECT VIDEO", "MP4 video URL detected."

        return "MEDIA URL", "File type is not immediately identifiable."

    except Exception:
        return "INVALID", "Could not analyze URL."


# ==========================================
# DOWNLOAD
# ==========================================

def download_subtitle(url):
    """Download a .vtt subtitle file directly into the downloads folder."""
    name = Path(unquote(urlparse(url).path)).name or "subtitles.vtt"
    name = re.sub(r'[<>:"/\\|?*]', "_", name)[:120]
    target = DOWNLOADS / name

    counter = 1
    while target.exists():
        target = DOWNLOADS / f"{Path(name).stem} ({counter}).vtt"
        counter += 1

    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read()

        target.write_bytes(data)
        print("\nSubtitle saved:", target)

        with open(HISTORY, "a", encoding="utf-8") as file:
            file.write(url + "\n")

    except Exception as error:
        print("\nSubtitle download failed:", error)


def download_video(url):
    status, message = analyze(url)

    print("\nSTATUS:", status)
    print(message)

    if status == "INVALID":
        print("\nThis link cannot be downloaded.")
        return

    if status == "SUBTITLE":
        download_subtitle(url)
        return

    if not YTDLP.exists():
        print("\nyt-dlp.exe was not found!")
        print("Expected:", YTDLP)
        return

    print("\nSending URL to yt-dlp...")
    print("Downloads folder:", DOWNLOADS)
    print("\n")

    command = [
        str(YTDLP),
        "--ignore-config",
        "--no-playlist",
        "--no-warnings",
        "--format", "best",
        "--output",
        str(DOWNLOADS / "%(title).80B [%(id)s].%(ext)s"),
        url
    ]

    try:
        result = subprocess.run(
            command,
            cwd=str(BASE_DIR),
            check=False
        )

        if result.returncode == 0:
            print("\nDownload completed!")
            with open(HISTORY, "a", encoding="utf-8") as file:
                file.write(url + "\n")
        else:
            print("\nDownload failed.")
            print("yt-dlp exit code:", result.returncode)

    except Exception as error:
        print("\nError:", error)


# ==========================================
# HISTORY
# ==========================================

def show_history():
    print("\n========== DOWNLOAD HISTORY ==========\n")

    if not HISTORY.exists():
        print("No download history yet.")
        return

    entries = HISTORY.read_text(encoding="utf-8").splitlines()

    if not entries:
        print("No download history yet.")
        return

    for number, entry in enumerate(entries, 1):
        print(f"{number}. {entry}")


# ==========================================
# OPEN DOWNLOADS
# ==========================================

def open_downloads():
    try:
        os.startfile(DOWNLOADS)
    except Exception as error:
        print("Could not open folder:", error)


# ==========================================
# MAIN MENU
# ==========================================

def main():
    if not YTDLP.exists():
        print("ERROR: yt-dlp.exe not found!")
        print("Expected location:", YTDLP)
        pause()
        return

    while True:
        banner()

        print(" [1] Analyze URL")
        print(" [2] Download authorized media")
        print(" [3] View download history")
        print(" [4] Open downloads folder")
        print(" [5] Exit")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            url = input("\nPaste URL: ").strip()
            status, message = analyze(url)
            print("\nSTATUS:", status)
            print(message)
            pause()

        elif choice == "2":
            url = input("\nPaste URL: ").strip()
            download_video(url)
            pause()

        elif choice == "3":
            show_history()
            pause()

        elif choice == "4":
            open_downloads()
            pause()

        elif choice == "5":
            print("\nVIDEOVAULT closed.")
            break

        else:
            print("\nInvalid option.")
            pause()


# ==========================================
# START
# ==========================================

if __name__ == "__main__":
    main()
