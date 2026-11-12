from main import game_init, GameStatus
from enum import Enum 

class CliMsgs(Enum):
    INVALID_INPUT = 1

def main():
    pass

class Cli:
    def __init__(self):
        self.to_print = None

    def __parse_input__(self, inp):
        move_player = inp[0]
        move_x = int(inp[1])
        move_y = int(inp[2])
        return move_player, move_x, move_y

    def prompt(self, inp):
        try:
            p, x, y = self.__parse_input__(inp)
            self.to_print = None
        except:
            self.to_print = CliMsgs.INVALID_INPUT
            

    def current_printed(self):
        return self.to_print