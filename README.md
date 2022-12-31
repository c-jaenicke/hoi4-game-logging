# Hearts Of Iron 4 - Game Logging Mod

This mod adds a decision to the game that automatically fires every month. When it fires, it writes country attributes to a file. After that you can run a script that parses the created file and turns it into a CSV file that can be imported into a excel like application and turned into graphs.

The logged attributes include:

- number of divisions
- amount of infantry equipment
- amount of ships
- manpower
- fuel
- number light tank divisions
- number medium tank divisions
- numbers heavy tank divisions

## Instructions

1. Subscribe to the mod on [Steam (steamcommunity.com)](https://steamcommunity.com/sharedfiles/filedetails/?id=2514115643)
1. Play a round of HoI4
1. Copy the file containing the logs, found in `Documents/Paradox Interactive/Hearts of Iron IV/logs/variable_dumps/game_logging.log` into a new folder
1. Move the `hoi4-log-parser-win-amd64.exe` into the same folder
1. Run the `hoi4-log-parser-win-amd64.exe`
1. Import the generated `csv.txt` into a excel like application

[Get the parser here](https://github.com/c-jaenicke/hoi4-game-logging/releases)

**Remeber to delete the `game_logging.log` file between runs! The next run will be appended to the
file if it is not deleted!**

## Disclaimer

**I am not responsible for any files going missing or being deleted by accident.**

## Code

[https://github.com/c-jaenicke/hoi4-game-logging](https://github.com/c-jaenicke/hoi4-game-logging)
