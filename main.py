ROWS = ['1', '2', '3']
COLS = ['_', 'A', 'B', 'C'] # the first col is index col


def clear_screen():
    '''
    The function clears the terminal screen.
    '''
    for _ in range(15):
        print("\033[F\033[K", end="")


def print_playground(playground):
    '''
    The function prints the current symbols from the list `playground`
    '''
    clear_screen()
    for row in playground:
        print(''.join(row))
    print()


def get_player_symbol(player):
    '''
    Replacing X and O with the corresponding emojis.
    '''
    return '❌ ' if player == 'x' else '⭕️ '


def player_turn(playground, player):
    '''
    The function take the input from player.
    It validate the input, if it in the correct format '2B'.
    If the input is correct, the function replace '🔳 ' with players symbol.
    At the end it calls the function `print_playground()` with new set symbol.
    '''
    while True:
        turn = input(f'Player {player}, your turn (i.e. "2B"): ').upper()
        if len(turn) != 2 or turn[0] not in ROWS or turn[1] not in COLS:
            print('😑 The input is invalid! Try again!')
        else:
            row = int(turn[0])
            col = COLS.index(turn[1])
            if playground[row][col] == '🔳 ':
                playground[row][col] = player
                print_playground(playground)
                break
            else:
                print("This cell is not empty. Try again!\n")


def winner_check(playground, player):
    '''
    The function take the playground and current player (his/her symbol) as input,
    and check all rows, cols and diagonals, if there are same '❌ ' or '⭕️ '.
    If there is a row of 3, the function returns True.
    '''
    for i in range(1, 4):
        if all(playground[i][j] == player for j in range(1, 4)):
            return True
        if all(playground[j][i] == player for j in range(1, 4)):
            return True
    if all(playground[i][i] == player for i in range(1, 4)) or \
       all(playground[i][4-i] == player for i in range(1, 4)):
        return True
    return False


def run_tic_tac_toe():
    '''
    Start the Tic-Tac-Toe game!
    '''
    playground = [['   ', '(A)', '(B)', '(C)'],['(1) ', '🔳 ', '🔳 ', '🔳 '],['(2) ', '🔳 ', '🔳 ', '🔳 '],['(3) ', '🔳 ', '🔳 ', '🔳 ']]

    print_playground(playground)
    print('\n👋 WELCOME TO THE TIC-TAC-TOE! 👋\n')

    p1 = None
    while not p1:
        p1 = input('   ❓ Choose the symbol for PLAYER 1 (send "O" or "X"): ').lower()
        if p1 not in ['x', 'o']:
            print('The choice is invalid! Try again...')
            p1 = None
    p2 = 'o' if p1 == 'x' else 'x'

    p1_symbol = get_player_symbol(p1)
    p2_symbol = get_player_symbol(p2)

    print(f"Player 1 has chosen {p1_symbol}, and starts the game.\n")
    print_playground(playground)

    player_won = False
    player = p1_symbol

    while not player_won:
        player_turn(playground, player)
        player_won = winner_check(playground, player)

        if player_won:
            print(f"   ✅ The player {player} won! 🥳\n")
        else:
            player = p2_symbol if player == p1_symbol else p1_symbol


def main():
    run_tic_tac_toe()


if __name__ == "__main__":
    main()
