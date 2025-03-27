#!/usr/bin/python3

def print_board(board):
    """
    Affiche le plateau de jeu.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Vérifie si un joueur a gagné.
    
    Parameters:
    board (list of list of str): Le plateau de jeu.

    Returns:
    bool: True si un joueur a gagné, False sinon.
    """
    # Vérifie les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérifie les colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérifie les diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """
    Vérifie si le plateau est plein.

    Parameters:
    board (list of list of str): Le plateau de jeu.

    Returns:
    bool: True si le plateau est plein, False sinon.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Fonction principale pour jouer au Tic-Tac-Toe.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board) and not is_board_full(board):
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if 0 <= row < 3 and 0 <= col < 3:
                if board[row][col] == " ":
                    board[row][col] = player
                    player = "O" if player == "X" else "X"
                else:
                    print("That spot is already taken! Try again.")
            else:
                print("Invalid input. Please enter row and column between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    print_board(board)
    if check_winner(board):
        print("Player " + ("O" if player == "X" else "X") + " wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
