# Space Explorer

Space Explorer is a small scrolling 2D game built with Pygame for the final project.

## Project Description

The player controls a spaceship in a world larger than the visible screen. The goal is to collect all stars in each level while avoiding three different types of moving enemies.

## Features

- Large scrolling game world with camera movement
- Player-controlled spaceship
- Three different enemy types with different movement patterns:
  - Patrol Enemy: moves back and forth horizontally
  - Chaser Enemy: moves toward the player
  - Bouncer Enemy: bounces around the world
- Collision detection
  - Colliding with enemies reduces player health
  - Collecting stars increases the score
- Two distinct levels
- Transition screen between levels
- Graphical images generated at startup if asset files are missing
- Packaged Python project with multiple modules

## How to Run

1. Install Python 3.
2. Install the required library:

```bash
pip install -r requirements.txt
```

3. Run the game:

```bash
python main.py
```

## Controls

- Arrow keys or WASD: Move the player
- Space: Continue to the next level after completing a level
- R: Restart after game over or victory
- Escape: Quit the game

