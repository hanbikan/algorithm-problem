import sys
input = sys.stdin.readline


def dfs(puttables, index, count):
    # Base case
    if index == len(puttables):
        global max_count
        max_count = max(max_count, count)
        return

    # Recursive case
    x, y = puttables[index]
    nx, ny = new_positions[x][y]
    if is_x_using[nx] == False and is_y_using[ny] == False:
        is_x_using[nx] = True
        is_y_using[ny] = True
        dfs(puttables, index+1, count+1)
        is_x_using[nx] = False
        is_y_using[ny] = False

    dfs(puttables, index+1, count)


if __name__ == '__main__':
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # Set new_positions
    new_positions = [[[-1, -1] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        new_positions[i][0] = [i, N-i-1]
        for j in range(1, N):
            new_positions[i][j][0] = new_positions[i][j-1][0] + 1
            new_positions[i][j][1] = new_positions[i][j-1][1] + 1

    # Set is_using
    is_x_using = [False]*(N*2-1)
    is_y_using = [False]*(N*2-1)

    # Set puttables
    puttables1 = []
    puttables2 = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                if (i+j) % 2 == 0:
                    puttables1.append((i, j))
                else:
                    puttables2.append((i, j))

    # Set total_count
    total_count = 0

    max_count = 0
    dfs(puttables1, 0, 0)
    total_count += max_count

    max_count = 0
    dfs(puttables2, 0, 0)
    total_count += max_count

    # Print the result
    print(total_count)
