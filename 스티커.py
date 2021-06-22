import sys
input = sys.stdin.readline


def getMaxScore(stickers, n):
    for j in range(n):
        for i in range(2):
            if j == 0:
                continue
            elif j == 1:
                stickers[i][j] += stickers[(i+1) % 2][j-1]
            else:
                stickers[i][j] += max(
                    stickers[(i+1) % 2][j-1],
                    stickers[(i+1) % 2][j-2],
                    stickers[i][j-2]
                )
    print(stickers)
    return max(max(stickers[0]), max(stickers[1]))


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        stickers = [list(map(int, input().split())),
                    list(map(int, input().split()))]

        maxScore = getMaxScore(stickers, n)
        print(maxScore)
