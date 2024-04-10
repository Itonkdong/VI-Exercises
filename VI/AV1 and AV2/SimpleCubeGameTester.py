from typing import Optional


class Player:
    def __init__(self):
        self.throws = []

    def add_throw(self, throw):
        self.throws.append(throw)

    def get_last_throw_score(self):
        last_throw = self.throws[-1]
        return sum(last_throw)

    def get_last_throw(self):
        return self.throws[-1]

    def tie_breaker_point(self):
        return self.throws[-1][0]


class DiceGame:
    __NUM_PLAYERS = 0

    def __init__(self):
        self.players = {}

    def add_player(self, player: Player):
        DiceGame.__NUM_PLAYERS += 1
        self.players[f"p{self.__NUM_PLAYERS}"] = player

    def __assign_values_to_players(self, values):
        for key in sorted(self.players.keys()):
            self.players[key].add_throw(values.pop(0))

    def dice_game(self, throws):

        for i in range(4):
            player = Player()
            player.add_throw(throws.pop(0))
            self.add_player(player)

        while True:
            outcome = self.play_game()
            if not outcome:
                self.__assign_values_to_players(throws)
                continue

            # print("Player to be deleted", outcome[0])

            del self.players[outcome]
            if len(self.players) == 1:
                break

            self.__assign_values_to_players(throws)

        for player in self.players.keys():
            return player

    def play_game(self) -> Optional[Player]:
        player_to_be_thrown = min(self.players.items(),
                                  key=lambda item: (item[1].get_last_throw_score(), item[1].tie_breaker_point()))
        additional_check = sorted(self.players.items(),
                                  key=lambda item: (item[1].get_last_throw_score(), item[1].tie_breaker_point()))

        player1 = additional_check[0][1]
        player2 = additional_check[1][1]
        # print(player1.get_last_throw(), player2.get_last_throw())

        if player1.get_last_throw() == player2.get_last_throw():
            return None
        return player_to_be_thrown[0]


game = DiceGame()
player_who_won = game.dice_game(
    [(6, 2), (4, 3), (3, 4), (5, 4), (3, 5), (1, 5), (4, 3), (1, 5), (1, 5), (5, 6), (2, 2)])
print("The game was won by", player_who_won)
