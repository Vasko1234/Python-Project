# Pygame Platformer Game

This is a platformer game developed using Pygame. The game features an overworld where the player can
switch between unlocked levels. To navigate the overworld, use the "a" key to go back a level and the"d"
key to go up a level. Press the spacebar to start the desired level. If the player dies, they will be brought
back to the overworld. Similarly, when the player completes a level, they will return to the overworld,
and the next level will be unlocked for play.

## Level Design

The current version of the game includes two separate levels: the first level and the second level. However,
please note that the additional levels beyond the second level utilize the same CSV files as the first level.
This repetition occurs because no new maps or level designs have been implemented yet. Future updates of the
game may introduce unique levels with distinctive challenges and layouts.

## Installation

1. Clone the repository: `git clone https://github.com/VaskoVelev/Python-Project.git`
2. Navigate to the project directory: `cd Python-Project`
3. Install the required dependencies: `pip install pygame`

## Usage

1. Open the `settings.py` file.
2. Locate the `graphics_color` variable.
3. Change the value of `graphics_color` to either "green" or "blue".
   - Example: `graphics_color = "green"` for green graphics.
4. Save the file.

## Controls

- Press the "a" key to go back a level in the overworld.
- Press the "d" key to go up a level in the overworld.
- Press the spacebar to start the current level.
- Use the "a" and "d" keys along with the spacebar to control the player in the level.

## Known Issues

The game is optimized to run at 240 frames per second (FPS). However, if the game is run
on a computer that cannot maintain at least 200 FPS, the game will feel slower and laggy.
Please ensure your computer meets the minimum requirements for a smooth gameplay experience.

## Author

- Vasil Velev №6 9a
- GitHub: [VaskoVelev](https://github.com/VaskoVelev)

Enjoy playing!