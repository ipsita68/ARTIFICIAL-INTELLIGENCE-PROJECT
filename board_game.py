def utility(board):
    # Calculate the utility for Player 1 (black coins)
    return board.count('B')


def is_terminal(board):
    # Check if there are no empty blocks on the board
    return '0' not in board


def actions(board):
    # Return a list of empty block indices
    return [i for i in range(len(board)) if board[i] == '0']


def result(board, action, player):
    # Place the player's coin on the selected block and update the board
    new_board = list(board)
    new_board[action] = 'B' if player == 1 else 'W'

    # Update adjacent blocks if needed
    for i in [-1, 1]:
        index = action + i
        while 0 <= index < len(board) and new_board[index] != '0' and new_board[index] != new_board[action]:
            new_board[index] = 'B' if player == 1 else 'W'
            index += i

    return ''.join(new_board)


def mini_max(board, depth, maximizing_player):
    if depth == 0 or is_terminal(board):
        return utility(board)

    if maximizing_player:
        max_eval = float('-inf')
        for action in actions(board):
            eval = mini_max(result(board, action, 1), depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for action in actions(board):
            eval = mini_max(result(board, action, 2), depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval


def main():
    # Read input as a string
    board = input("Enter the board configuration: ")

    # Set the depth according to the size of the board
    depth = len(board)

    # Calculate and print the utility of Player 1 (Player MAX)
    print("Utility of Player 1:", mini_max(board, depth, True))


if __name__ == "__main__":
    main()
