# Baseball Team Manager

A command-line application for managing baseball team lineups, player statistics, and game scheduling.

## Overview

The Baseball Team Manager is a Python-based tool that helps coaches and team managers organize their baseball lineups, track player statistics, and manage game dates. The application allows you to add, remove, and rearrange players in your lineup while maintaining their positions and batting statistics.

## Features

- **Team Lineup Management**: View, add, remove, and reorganize players in your team's batting lineup
- **Player Tracking**: Store player information including name, position, and batting statistics
- **Batting Statistics**: Automatically calculate and display batting averages (hits/at-bats)
- **Game Scheduling**: Input and track upcoming game dates with countdown functionality
- **Data Persistence**: Save and load player data from CSV files
- **Position Management**: Assign and modify player positions (C, 1B, 2B, 3B, SS, LF, CF, RF, P)

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone or download the project files to your local machine
Option A – Clone using Git:
https://github.com/amardeepsingh01/bassball

git clone https://github.com/amardeepsingh01/bassball.git

Option B – Download ZIP:
-Click the green Code button on the GitHub page
-Select Download ZIP
-Extract the files to your desired location

3. No additional packages need to be installed

## Usage

### Starting the Application

Run the main program:
```bash
python main.py
```

### Menu Options

Once the application starts, you'll be prompted to enter the next game date (YYYY-MM-DD format), and then you can choose from the following options:

1. **Display Lineup** - View all players in the current lineup with their statistics
2. **Add Player** - Add a new player to the lineup
3. **Remove Player** - Remove a player from the lineup
4. **Move Player** - Rearrange player order in the lineup
5. **Edit Position** - Change a player's field position
6. **Edit Stats** - Update a player's at-bats and hits statistics
7. **Exit** - Save changes and exit the application

### Lineup Display Format

The lineup is displayed in a formatted table showing:
- **Player#** - Position in lineup
- **Player Name** - First and last name
- **POS** - Field position (C, 1B, 2B, 3B, SS, LF, CF, RF, P)
- **AB** - At-bats (total plate appearances)
- **H** - Hits (successful hits)
- **AVG** - Batting average (hits ÷ at-bats)

Example:
```
Player               POS    AB     H     AVG
1   John Smith       C      34     5     0.147
2   Jane Doe         CF     45     12    0.267
```

## Project Structure

```
baseball_mideterm/
├── main.py          # Main application entry point and game loop
├── objects.py       # Player and Lineup classes
├── db.py            # Database functions for loading/saving player data
├── ui.py            # User interface display functions
├── players.csv      # Data file storing player information
└── README.md        # This file
```

## Data Format

Player data is stored in `players.csv` with the following format:

```
FirstName,LastName,Position,AtBats,Hits
```

Example:
```
John,Smith,C,34,5
Jane,Doe,CF,45,12
```

## Classes

### Player
Represents a single player with the following attributes:
- `first_name`: Player's first name
- `last_name`: Player's last name
- `position`: Field position (C, 1B, 2B, 3B, SS, LF, CF, RF, P)
- `at_bats`: Total plate appearances
- `hits`: Total successful hits
- `batting_average`: Calculated property (hits / at_bats)

### Lineup
Manages a list of players with methods to:
- Add/remove players
- Move players to different positions in the lineup
- Update player positions and statistics
- Iterate through players

## Field Positions

- **C** - Catcher
- **1B** - First Base
- **2B** - Second Base
- **3B** - Third Base
- **SS** - Shortstop
- **LF** - Left Field
- **CF** - Center Field
- **RF** - Right Field
- **P** - Pitcher

## Notes

- All changes are automatically saved to `players.csv` when you exit the application
- Batting averages are rounded to three decimal places
- Game date countdown is calculated based on the system's current date
- The application handles invalid date formats gracefully

## License

This is a midterm project for a Python course.
