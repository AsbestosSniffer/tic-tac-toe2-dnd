from game import GameStatus
from enum import Enum 

class CliMsgs(Enum):
    INVALID_INPUT = 1,
    PLAYER1_WIN = 2,
    PLAYER2_WIN = 3,
    DRAW = 4,
    WRONG_PLAYER_TURN = 5

def main():
    pass

class Cli:
    def __init__(self, game):
        self.to_print = None
        self.game = game
        self.player1 = self.game.player_init()
        self.player2 = self.game.player_init()

    def __parse_input__(self, inp):
        move_player = inp[0]
        move_x = int(inp[1])
        move_y = int(inp[2])
        return move_player, move_x, move_y

    def prompt(self, inp):
        self.to_print = None 

        try:
            p_char, x, y = self.__parse_input__(inp)
        except:
            self.to_print = CliMsgs.INVALID_INPUT
            return 
        
        if p_char == 'x':
            if not self.player1.place_mark(x, y):
                self.to_print = CliMsgs.WRONG_PLAYER_TURN
        else:
            if not self.player2.place_mark(x, y):
                self.to_print = CliMsgs.WRONG_PLAYER_TURN

        match self.game.get_result():
            case GameStatus.PLAYER1_WINS:
                self.to_print = CliMsgs.PLAYER1_WIN
            case GameStatus.PLAYER2_WINS:
                self.to_print = CliMsgs.PLAYER2_WIN
            case GameStatus.DRAW:
                self.to_print = CliMsgs.DRAW
        
    def get_to_print(self):
        return self.to_print