# 3.3 Moving Ball Game

An interactive game built with **Pygame** featuring a red ball that moves around the screen using arrow keys.

## Features

- Red ball (radius 25px) centered on a white 600×600 canvas
- Arrow key controls — each press moves the ball **20 pixels**
- Boundary detection — the ball cannot leave the screen edges
- Smooth animation at **60 FPS**

## Project Structure

```
Practice7/
└── moving_ball/
    ├── main.py   # Game loop, event handling, rendering
    ├── ball.py   # Ball class (movement & drawing logic)
    └── README.md
```

## Requirements

- Python 3.x
- Pygame

Install Pygame:

```bash
pip install pygame
```

## How to Run

```bash
cd Practice7/moving_ball
python main.py
```

## Controls

| Key        | Action      |
|------------|-------------|
| ↑ Arrow    | Move Up     |
| ↓ Arrow    | Move Down   |
| ← Arrow    | Move Left   |
| → Arrow    | Move Right  |

## Implementation Notes

- `Ball` class in `ball.py` encapsulates position, color, radius, and movement logic.
- `move()` checks boundary conditions **before** updating position — invalid moves are silently ignored.
- `main.py` handles the Pygame event loop and delegates rendering to `Ball.draw()`.