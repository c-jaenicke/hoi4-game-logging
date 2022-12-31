# Hearts Of Iron 4 - Gameplay Logging Mod

This mod adds a decision to the game that automatically fires every month. When it fires, it
writes country attributes to a file. This repo contains a script that parses the created file and
turns it into a CSV file that can be imported into a excel like application and turned into graphs.

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

1. Subscribe to the mod on [Steam]()
1. Play a round of HoI4
1. Copy the file containing the logs, found in `Documents/Paradox Interactive/Hearts of Iron IV/logs/variable_dumps/game_logging.log` into a new folder
1. Move the `parser.exe` into the same folder
1. run the `parser.exe`
1. import the generated `csv.txt` into a excel like application

## DISCLAIMER

**I am not responsible for any files going missing or being deleted by accident.**
