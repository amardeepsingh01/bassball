def display_menu(positions):
    print("\nMenu Options")
    print("1 – Display lineup")
    print("2 – Add player")
    print("3 – Remove player")
    print("4 – Move player")
    print("5 – Edit position")
    print("6 – Edit stats")
    print("7 – Exit")
    print("\nPOSITIONS")
    print(", ".join(positions))
    print("=" * 64)

def display_lineup(lineup):
    print(" Player               POS    AB     H     AVG")
    print("-" * 64)

    for i, player in enumerate(lineup, start=1):
        print(f"{i:<3} "
              f"{player.full_name:<20} "
              f"{player.position:<5} "
              f"{player.at_bats:<6} "
              f"{player.hits:<6} "
              f"{player.batting_average:.3f}")


