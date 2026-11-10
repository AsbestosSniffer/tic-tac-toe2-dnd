def main():
    print('Hello World!')

class Player:
    def __init__(self):
        self.is_my_turn = True

    def place_mark(self, x, y):
        if self.is_my_turn:
            self.is_my_turn = False
            return True
        return False

def player_init():
    player = Player()
    return player

if __name__ == '__main__':
    main()