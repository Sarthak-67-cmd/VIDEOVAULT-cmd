<div align="center">

# 🎬 VIDEOVAULT CMD

**Your tiny Windows command-line sidekick for saving videos and subtitles you're allowed to keep.**

![Python](https://img.shields.io/badge/python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-0078D6?style=for-the-badge)
![Powered by yt-dlp](https://img.shields.io/badge/powered%20by-yt--dlp-red?style=for-the-badge)
![Works on my machine](https://img.shields.io/badge/works%20on-my%20machine-brightgreen?style=for-the-badge)
![Approved by (https://img.shields.io/badge/approved%20by-me%2C%20myself%20%26%20I-ff69b4?style=for-the-badge)
![Made with](https://img.shields.io/badge/made%20with-%E2%98%95%20%26%20bugs-orange?style=for-the-badge)

</div>

---

## ✨ What it does

- 🔍 **Analyze** a link (direct MP4, HLS playlist, VTT subtitle...)
- ⬇️ **Download** videos through yt-dlp
- 💬 **Grab `.vtt` subtitles** directly
- 📜 **Remember** everything in `history.txt`
- 📂 **Open** your downloads folder with one keypress

## 🧰 What you need

- 💻 Windows, macOS or Linux
- 🐍 Python 3.8 or newer
- 📦 yt-dlp from the [official releases page](https://github.com/yt-dlp/yt-dlp/releases): `yt-dlp.exe` on Windows, `yt-dlp_macos` on Mac

## 🚀 Quick start

1. Clone or download this repo.
2. Drop the yt-dlp file next to `videovault.py`.
3. Run it:

```bash
python videovault.py      # Windows
python3 videovault.py     # Mac / Linux
```

🍎 **Mac users:** make the downloaded file runnable first:

```bash
chmod +x yt-dlp_macos
```

If macOS blocks it, go to System Settings > Privacy & Security and click **Allow Anyway**.

VIDEOVAULT hunts for yt-dlp in its own folder first, then any `yt-dlp*` file, then your system PATH (so `brew install yt-dlp` works on Mac too). It's a good sniffer.

## 🎮 The menu

```
[1] Analyze URL
[2] Download authorized media
[3] View download history
[4] Open downloads folder
[5] Exit
```

Pick a number, paste an HTTPS link, and your file lands in `downloads/`. Easy.

## 🗂️ What's inside

```
videovault.py   # the whole app 🧠
downloads/      # your loot (auto-created) 🎒
history.txt     # list of past downloads (auto-created) 📖
yt-dlp.exe      # bring your own 🔧
```

## 🚧 Good to know

- 🔒 HTTPS links only.
- 📼 One video per link (playlists are skipped on purpose).
- 🛡️ **DRM-protected videos won't work.** yt-dlp doesn't decrypt DRM, and this project doesn't try to get around it.

## ⚖️ Be cool, follow the rules

Only download things you own, things that are freely licensed, or things you have permission to save. You're responsible for following each site's terms and your local copyright laws. If a platform has an official offline download button, use that instead.

## 🙌 Credits

Built on the shoulders of [yt-dlp](https://github.com/yt-dlp/yt-dlp). Huge thanks to its maintainers.

## 📄 License

Add a `LICENSE` file (MIT is a popular, friendly choice).

---

<div align="center">⭐ If this helped, give the repo a star! ⭐</div>
