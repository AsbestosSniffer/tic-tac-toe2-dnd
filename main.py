def main():
    print('Hello World!')

class Game:
    def __init__(self):
        self.player_num = 1
        self.player_turn = 1
        # 0 indicates empty, 1 indicates occupied
        self.grid = [[0 for _ in range(3)] for _ in range(3)]

    def player_init(self):
        player = Player(self, self.player_num)
        self.player_num = 2
        return player

    def change_turn(self):
        self.player_turn = 3 - self.player_turn

    def current_player_id(self):
        return self.player_turn 
    
class Player:
    def __init__(self, game, id):
        self.id = id
        self.game = game

    def place_mark(self, x, y):
        if self.game.current_player_id() == self.id \
            and self.game.grid[x][y] == 0:
            self.game.grid[x][y] = 1
            self.game.change_turn()
            return True
        return False

def game_init():
    return Game()


if __name__ == '__main__':
    main()