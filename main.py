def main():
    print('Hello World!')

class Game:
    def __init__(self):
        self.player_num = 1

    def player_init(self, x):
        player = Player(self.player_num)
        self.player_num = 2
        return player

class Player:
    def __init__(self, x):
        self.is_my_turn = x == 1

    def place_mark(self, x, y):
        if self.is_my_turn:
            self.is_my_turn = False
            return True
        return False

def game_init():
    return Game()


if __name__ == '__main__':
    main()