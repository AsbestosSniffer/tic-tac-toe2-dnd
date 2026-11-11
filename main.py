from itertools import chain
from enum import Enum

def main():
    print('Hello World!')

class GameStatus(Enum):
    PLAYER1_WINS = 1
    PLAYER2_WINS = 2
    DRAW = 3

class Game:
    def __init__(self):
        self.player_num = 1
        self.player_turn = 1
        # 0 indicates empty, 1 indicates occupied
        self.grid = [[0 for _ in range(3)] for _ in range(3)]
        self.row_counter = [0, 0, 0]
        self.col_counter = [0, 0, 0]
        self.diag_counter = [0, 0]

        self.status = GameStatus.PLAYER1_WINS 

    def get_status(self):
        return self.status

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

    def is_valid_move(self, x, y):
        res = True
        res &= self.game.current_player_id() == self.id
        res &= self.game.grid[x][y] == 0
        res &= all(x < 3 for x in chain(self.game.row_counter, self.game.col_counter, self.game.diag_counter))
        return res

    def update_state(self, x, y):
        self.game.grid[x][y] = 1
        self.game.row_counter[x] += 1
        self.game.col_counter[y] += 1
        if x == y:
            self.game.diag_counter[0] += 1
        if x == 2-y:
            self.game.diag_counter[1] += 1
        self.game.change_turn()

    def place_mark(self, x, y):
        if self.is_valid_move(x, y):
            self.update_state(x, y)
            return True
        return False

def game_init():
    return Game()


if __name__ == '__main__':
    main()