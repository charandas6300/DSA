# import random

# def print_board(board):
#     print("---------")
#     for row in board:
#         print("|", end=" ")
#         for cell in row:
#             print(cell, end=" | ")
#         print("\n---------")

# def check_winner(board):
#     # Check rows
#     for row in board:
#         if len(set(row)) == 1 and row[0] != " ":
#             return row[0]
    
#     # Check columns
#     for col in range(3):
#         if len(set([board[row][col] for row in range(3)])) == 1 and board[0][col] != " ":
#             return board[0][col]
    
#     # Check diagonals
#     if board[0][0] == board[1][1] == board[2][2] != " ":
#         return board[0][0]
#     if board[0][2] == board[1][1] == board[2][0] != " ":
#         return board[0][2]
    
#     return None

# def get_empty_cells(board):
#     empty_cells = []
#     for row in range(3):
#         for col in range(3):
#             if board[row][col] == " ":
#                 empty_cells.append((row, col))
#     return empty_cells

# def make_computer_move(board):
#     empty_cells = get_empty_cells(board)
#     row, col = random.choice(empty_cells)
#     board[row][col] = "O"

# def make_user_move(board):
#     while True:
#         move = input("Enter your move (row col): ")
#         try:
#             row, col = map(int, move.split())
#             if board[row][col] == " ":
#                 board[row][col] = "X"
#                 break
#             else:
#                 print("That cell is already occupied. Try again.")
#         except ValueError:
#             print("Invalid input. Try again.")

# def play_game():
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     print("Welcome to Tic-Tac-Toe!")
#     print_board(board)

#     while True:
#         make_user_move(board)
#         print_board(board)
#         winner = check_winner(board)
#         if winner:
#             print(f"Congratulations! {winner} wins!")
#             break

#         if len(get_empty_cells(board)) == 0:
#             print("It's a tie!")
#             break

#         make_computer_move(board)
#         print("Computer's move:")
#         print_board(board)
#         winner = check_winner(board)
#         if winner:
#             print(f"Sorry! {winner} wins!")
#             break

#         if len(get_empty_cells(board)) == 0:
#             print("It's a tie!")
#             break

# play_game()
##############################################################################################################3
# def print_board(board):
#     for i in range(0, 9, 3):
#         print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")
#         if i < 6:
#             print("-----------")

# def is_winner(board, player):
#     winning_combinations = [
#         [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
#         [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
#         [0, 4, 8], [2, 4, 6]              # Diagonals
#     ]
    
#     for combination in winning_combinations:
#         if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
#             return True
#     return False

# def play_tic_tac_toe():
#     board = [str(i) for i in range(1, 10)]
#     current_player = 'X'
#     game_over = False

#     while not game_over:
#         print_board(board)
#         print(f"\nPlayer {current_player}'s turn.")
#         position = input("Choose a position (1-9): ")

#         if not position.isdigit() or int(position) not in range(1, 10):
#             print("Invalid position. Please try again.")
#             continue

#         position = int(position) - 1

#         if board[position] != 'X' and board[position] != 'O':
#             board[position] = current_player

#             if is_winner(board, current_player):
#                 print_board(board)
#                 print(f"\nPlayer {current_player} wins!")
#                 game_over = True
#             elif all([cell == 'X' or cell == 'O' for cell in board]):
#                 print_board(board)
#                 print("\nThe game ends in a tie!")
#                 game_over = True
#             else:
#                 current_player = 'O' if current_player == 'X' else 'X'
#         else:
#             print("That position is already occupied. Please try again.")

# play_tic_tac_toe()
import random

def print_board(board):
    for i in range(0, 9, 3):
        print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")
        if i < 6:
            print("-----------")

def is_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
    return False

def get_player_move(board):
    while True:
        position = input("Choose a position (1-9): ")

        if not position.isdigit() or int(position) not in range(1, 10):
            print("Invalid position. Please try again.")
            continue

        position = int(position) - 1

        if board[position] != 'X' and board[position] != 'O':
            return position
        else:
            print("That position is already occupied. Please try again.")

def get_computer_move(board):
    available_positions = [i for i in range(9) if board[i] != 'X' and board[i] != 'O']
    return random.choice(available_positions)

def play_tic_tac_toe():
    board = [str(i) for i in range(0, 9)]
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board(board)

        if current_player == 'X':
            print(f"\nPlayer {current_player}'s turn.")
            position = get_player_move(board)
        else:
            print(f"\nComputer's turn.")
            position = get_computer_move(board)
        
        board[position] = current_player

        if is_winner(board, current_player):
            print_board(board)
            if current_player == 'X':
                print(f"\nPlayer {current_player} wins!")
            else:
                print("\nComputer wins!")
            game_over = True
        elif all([cell == 'X' or cell == 'O' for cell in board]):
            print_board(board)
            print("\nThe game ends in a tie!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'

play_tic_tac_toe()
