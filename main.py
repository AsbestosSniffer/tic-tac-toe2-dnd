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

        self.result = None

    def get_result(self):
        return self.result

    def player_init(self):
        player = Player(self, self.player_num)
        self.player_num = 2
        return player

    def change_turn(self):
        self.player_turn = 3 - self.player_turn

    def current_player_id(self):
        return self.player_turn 

    def check_gameover(self):
        if any(x == 3 for x in chain(self.row_counter, self.col_counter, self.diag_counter)):
            self.result = GameStatus.PLAYER1_WINS
        elif any(x == -3 for x in chain(self.row_counter, self.col_counter, self.diag_counter)):
            self.result = GameStatus.PLAYER2_WINS
    
class Player:
    def __init__(self, game, id):
        self.id = id
        self.game = game
        self.increment = 1 if self.id == 1 else -1

    def is_valid_move(self, x, y):
        res = True
        res &= self.game.current_player_id() == self.id
        res &= self.game.grid[x][y] == 0
        res &= self.game.get_result() is None 
        return res

    def update_state(self, x, y):
        self.game.grid[x][y] = 1
        self.game.row_counter[x] += self.increment
        self.game.col_counter[y] += self.increment
        if x == y:
            self.game.diag_counter[0] += self.increment
        if x == 2-y:
            self.game.diag_counter[1] += self.increment
        self.game.check_gameover()
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