import sys

input = sys.stdin.readline
NONE, X, O = 0, 1, 2

def find_winner():
    for i in range(3):
        if grid[i][0] != NONE and grid[i][0] == grid[i][1] == grid[i][2]:
            return grid[i][0]

    for j in range(3):
        if grid[0][j] != NONE and grid[0][j] == grid[1][j] == grid[2][j]:
            return grid[0][j]

    if grid[0][0] != NONE and grid[0][0] == grid[1][1] == grid[2][2]:
        return grid[0][0]

    if grid[0][2] != NONE and grid[0][2] == grid[1][1] == grid[2][0]:
        return grid[0][2]

    return NONE

def find_winner_recursively(turn, put_count):
    winner = find_winner()
    if winner != NONE:
        return winner
    if put_count == 9:
        return NONE

    winners = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] != NONE:
                continue
            grid[i][j] = turn
            winner = find_winner_recursively(turn % 2 + 1, put_count + 1)
            grid[i][j] = NONE

            if winner == turn:
                return winner
            winners.append(winner)

    # I can't win
    for winner in winners:
        if winner == NONE:
            return NONE

    return turn % 2 + 1

def print_grid():
    for i in range(3):
        for j in range(3):
            if grid[i][j] == X:
                print("X", end=" ")
            elif grid[i][j] == O:
                print("O", end=" ")
            else:
                print(" ", end=" ")
        print()

grid = [list(map(int, input().split())) for _ in range(3)]

put_count = 0
for i in range(3):
    for j in range(3):
        if grid[i][j] != NONE:
            put_count += 1

turn = X if put_count % 2 == 0 else O
winner = find_winner_recursively(turn, put_count)
if turn == winner:
    print("W")
elif winner == NONE:
    print("D")
else:
    print("L")