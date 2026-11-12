from main import game_init, GameStatus
from enum import Enum 

class CliMsgs(Enum):
    INVALID_INPUT = 1,
    PLAYER1_WIN = 2

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
        try:
            p_char, x, y = self.__parse_input__(inp)
            self.to_print = None
        except:
            self.to_print = CliMsgs.INVALID_INPUT
            return 
        
        if p_char == 'x':
            self.player1.place_mark(x, y)
        else:
            self.player2.place_mark(x, y)

        match self.game.get_result():
            case GameStatus.PLAYER1_WINS:
                self.to_print = CliMsgs.PLAYER1_WIN
        
    def current_printed(self):
        return self.to_print