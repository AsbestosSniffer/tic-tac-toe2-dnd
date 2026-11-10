def main():
    print('Hello World!')

class Game:
    def player_init(self, x):
        return Player(x)

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

def player_init(x):
    player = Player(x)
    return player


if __name__ == '__main__':
    main()