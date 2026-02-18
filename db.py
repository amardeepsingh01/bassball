import csv , os
from objects import Player

BASE_DIR = os.path.dirname(__file__)
FILENAME = os.path.join(BASE_DIR, "players.csv")


def load_players():
    players = []
    try:
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 5:

                    player = Player(
                        row[0],          # first name
                        row[1],          # last name
                        row[2],          # position
                        int(row[3]),     # at bats
                        int(row[4])      # hits
                    )
                    players.append(player)

    except FileNotFoundError:
        print("File not found. Starting empty lineup.")

    return players



def save_players(lineup):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        for player in lineup:
            writer.writerow([
                player.first_name,
                player.last_name,
                player.position,
                player.at_bats,
                player.hits
            ])
