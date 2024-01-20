import random

def print_board(board):
    for i in range(0, 9, 3):
        print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")
        if i<6:
            print("--------")

def is_winner(board,player):
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8], 
    [0, 4, 8], [2, 4, 6]]

    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
    return False

def get_player_move(board):
    while True:
        position = input("Enter the position where you want to perform the task")

        if not position.isdigit() or int(position) not in range(0, 9):
            print("invalid")
            continue

        position = int(position) 

        if board[position] != 'X' and board[position] != 'O':
            return position
        else: 
            print("Already occupied")

def get_computer_move(board):
    available_positions = [i for i in range(9) if board[i]!='X' and board[i]!='O']
    return random.choice(available_positions)

def play_tic_tac_toe():
    board = [str(i) for i in range(0,9)]
    current_player = 'X'
    game_over = False

    while not game_over:
        #print board state
        print_board(board)

        if current_player == 'X':
            print(f"{current_player}'s turn")
            move = get_player_move(board)
        else: 
            print('Computer\'s Turn')
            move = get_computer_move(board)

        board[move] = current_player

        if is_winner(board, current_player):
            print_board(board)

            if current_player == 'X':
                print(f"Congratulations! {current_player} won!")
            else:
                print("computer won") 
            game_over = True
        elif all(cell=='X' or cell=='O' for cell in board):
            print_board(board)
            print("it's a tie game")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'

play_tic_tac_toe()                