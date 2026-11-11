from main import game_init, GameStatus

def main():
    game = game_init()
    player1 = game.player_init()
    player2 = game.player_init()

    done = False
    while not done:
        for r in game.grid:
            print(r)
            
        inp = input("input like 'X12' or 'O00'")
        try:
            symbol, r, c = inp[0], int(inp[1]), int(inp[2])
        except:
            print("incorrect input format")

        if symbol in ['x','X']:
            try:
                player1.place_mark(r, c)
            except:
                print("invalid move")
        elif symbol in ['o', 'O']:
            try:
                player2.place_mark(r, c)
            except:
                print("invalid move")
        else:
            print("incorrect player symbol")

        game.check_gameover()
        done = game.get_result()

    if done == GameStatus.PLAYER1_WINS:
        print("player 1 wins")
    elif done == GameStatus.PLAYER2_WINS:
        print("player 2 wins")
    else:
        print("draw")

if __name__ == "__main__":
    main()