board = [' ' for i in range(9)]

def print_state(state):
    for (i, c) in enumerate(board):
        if (i+1) % 3 == 0:
            print(f'{c}')
        else:
            print(f'{c}|', end='')
print_state(board)

win_comb = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (1, 4, 7), (2, 4, 6), (1, 4, 7), (0, 3, 6), (2, 5, 8)]

def is_win_comb(state, comb):
    for (x, y, z) in comb:
        if (state[x] == state[y] and state[x] == state[z]) and (state[x] == 'X' or state[x] == 'O'):
            return state[x]
        else:
            return ''

def play(board):
    sign_move = 'X'
    num_dict = []
    while is_win_comb(board, win_comb) == '':
        num_cell = int(input(f'Куда хотите поставить {sign_move}: '))
        print(*num_dict)
        if num_cell in num_dict:
            print('Неа')
            continue
        else:
            num_dict.append(num_cell)
            board[num_cell - 1] = sign_move
            print_state(board)
        winner_sign = is_win_comb(board, win_comb)
        if winner_sign != '':
            print(f'sign {sign_move} win')
            break
        if sign_move != 'X':
            sign_move = 'X'
        else:
            sign_move = 'O'

play(board)

