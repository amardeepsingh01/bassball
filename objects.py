class Player:

    def __init__(self, first_name, last_name, position, at_bats, hits):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.at_bats = int(at_bats)
        self.hits = int(hits)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def batting_average(self):
        if self.at_bats == 0:
            return 0.0
        return round(self.hits / self.at_bats, 3)

class Lineup:

    def __init__(self):
        self.__players = []   # private list (encapsulation)

    def add_player(self, player):
        self.__players.append(player)

    def remove_player(self, index):
        return self.__players.pop(index)

    def move_player(self, old_index, new_index):
        player = self.__players.pop(old_index)
        self.__players.insert(new_index, player)

    def get_player(self, index):
        return self.__players[index]

    def update_position(self, index, new_position):
        self.__players[index].position = new_position

    def update_stats(self, index, at_bats, hits):
        self.__players[index].at_bats = at_bats
        self.__players[index].hits = hits

    def __len__(self):
        return len(self.__players)

    def __iter__(self):      # REQUIRED FOR 3 MARKS
        return iter(self.__players)
