from objects import Player, Lineup
from db import load_players, save_players
from ui import display_menu, display_lineup

POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")


def main():

    lineup = Lineup()

    # Load players into lineup
    players = load_players()
    for player in players:
        lineup.add_player(player)

    while True:
        display_menu(POSITIONS)
        choice = input("Menu option: ")

        # 1 - Display lineup
        if choice == "1":
            display_lineup(lineup)

        # 2 - Add player
        elif choice == "2":
            first = input("First name: ")
            last = input("Last name: ")

            while True:
                pos = input("Position: ").upper()
                if pos in POSITIONS:
                    break
                print("Invalid position.")

            try:
                at_bats = int(input("At bats: "))
                hits = int(input("Hits: "))

                if at_bats < 0 or hits < 0:
                    print("Numbers cannot be negative.")
                elif hits > at_bats:
                    print("Hits cannot exceed at bats.")
                else:
                    player = Player(first, last, pos, at_bats, hits)
                    lineup.add_player(player)
                    save_players(lineup)
                    print(f"{player.full_name} was added.")

            except ValueError:
                print("Invalid number entered.")

        # 3 - Remove player
        elif choice == "3":
            try:
                number = int(input("Lineup number: "))
                removed = lineup.remove_player(number - 1)
                save_players(lineup)
                print(f"{removed.full_name} was deleted.")
            except (ValueError, IndexError):
                print("Invalid selection.")

        # 4 - Move player
        elif choice == "4":
            try:
                current = int(input("Current lineup number: "))
                new = int(input("New lineup number: "))
                lineup.move_player(current - 1, new - 1)
                save_players(lineup)
                print(f"{lineup.get_player(new - 1).full_name} was moved.")
            except (ValueError, IndexError):
                print("Invalid selection.")

        # 5 - Edit position
        elif choice == "5":
            try:
                number = int(input("Lineup number: "))

                while True:
                    pos = input("New position: ").upper()
                    if pos in POSITIONS:
                        break
                    print("Invalid position.")

                lineup.update_position(number - 1, pos)
                save_players(lineup)
                print(f" {lineup.get_player(number - 1).full_name} was updated.")

            except (ValueError, IndexError):
                print("Invalid selection.")

        # 6 - Edit stats
        elif choice == "6":
            try:
                number = int(input("Lineup number: "))
                at_bats = int(input("New at bats: "))
                hits = int(input("New hits: "))

                if at_bats < 0 or hits < 0:
                    print("Numbers cannot be negative.")
                elif hits > at_bats:
                    print("Hits cannot exceed at bats.")
                else:
                    lineup.update_stats(number - 1, at_bats, hits)
                    save_players(lineup)
                    print("Stats updated.")

            except (ValueError, IndexError):
                print("Invalid input.")

        # 7 - Exit
        elif choice == "7":
            save_players(lineup)
            print("Bye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
