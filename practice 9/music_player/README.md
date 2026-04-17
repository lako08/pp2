# 🎵 Music Player with Keyboard Controller

A terminal-style Pygame music player with animated waveform UI, playlist management, and full keyboard control.

---

## Features

| Feature | Detail |
|---|---|
| Playback | Play, Stop, Next, Previous |
| Auto-advance | Moves to next track when current ends |
| Progress bar | Animated playback position indicator |
| Waveform | Animated bar visualizer (reacts to playback state) |
| Playlist | Auto-loads all `.wav` `.mp3` `.ogg` `.flac` from `./music/` |
| Flash messages | On-screen feedback for every key action |

---

## Project Structure

```
Practice7/
└── music_player/
    ├── main.py                   # Game loop, UI rendering
    ├── player.py                 # MusicPlayer class (playback logic)
    ├── generate_test_tracks.py   # Utility: create sample WAV tones
    ├── music/
    │   ├── track1.wav            # (add your own audio files here)
    │   └── track2.wav
    └── README.md
```

---

## Requirements

- Python 3.10+
- Pygame

```bash
pip install pygame
```

---

## Quick Start

### 1. Add audio files
Drop `.wav`, `.mp3`, `.ogg`, or `.flac` files into the `music/` folder.

**Or generate test tones automatically:**

```bash
cd Practice7/music_player
python generate_test_tracks.py   # creates music/track1.wav and track2.wav
```

### 2. Run the player

```bash
cd Practice7/music_player
python main.py
```

---

## Keyboard Controls

| Key | Action |
|-----|--------|
| `P` | ▶ Play / Resume |
| `S` | ■ Stop |
| `N` | ⏭ Next track |
| `B` | ⏮ Previous (Back) track |
| `Q` | ✕ Quit |

---

## Architecture

### `player.py` — `MusicPlayer` class

| Method | Description |
|--------|-------------|
| `_load_playlist()` | Scans `./music/` for supported audio files |
| `play()` | Loads and plays the current track via `pygame.mixer.music` |
| `stop()` | Stops playback, resets position |
| `next_track()` | Advances index (wraps around), plays next |
| `prev_track()` | Decrements index (wraps around), plays previous |
| `update()` | Called each frame — detects end-of-track, auto-advances |
| `get_position()` | Returns elapsed seconds using wall-clock math |

### `main.py` — UI & event loop

- **Header bar** with title
- **Animated waveform** (32 bars, sine-driven animation while playing)
- **Track panel** — name, playlist position, status badge, elapsed time, progress bar
- **Flash messages** — fade-out feedback on key presses
- **Shortcut row** — keyboard hints always visible at the bottom

---

## Notes

- `pygame.mixer.music.get_length()` is unreliable for some MP3s — the progress bar uses a 3-minute demo cycle visually, while actual elapsed time is tracked precisely.
- The player wraps around at both ends of the playlist.
- Files are sorted alphabetically when loaded.