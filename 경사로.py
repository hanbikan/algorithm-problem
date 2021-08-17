import sys
input = sys.stdin.readline


def getPossiblePathCount():
    possiblePathCount = 0

    # 가로
    for i in range(N):
        isValidPath = True
        isRunwayPut = [False]*N

        for j in range(N-1):
            c, n = heights[i][j], heights[i][j+1]

            # 같을 경우
            if c == n:
                continue

            # 1 2
            elif c+1 == n:
                flag = True

                # 경사로 놓기
                for k in range(j-L+1, j+1):
                    if k < 0 or heights[i][k] != c or isRunwayPut[k] == True:
                        flag = False
                        break
                    else:
                        isRunwayPut[k] = True

                # 경사로 놓기에 실패
                if not flag:
                    isValidPath = False
                    break
            # 2 1
            elif c == n+1:
                flag = True

                # 경사로 놓기
                for k in range(j+1, j+L+1):
                    if k > N-1 or heights[i][k] != n or isRunwayPut[k] == True:
                        flag = False
                        break
                    else:
                        isRunwayPut[k] = True

                # 경사로 놓기에 실패
                if not flag:
                    isValidPath = False
                    break

            # 높이 차이가 2 이상
            else:
                isValidPath = False
                break

        if isValidPath:
            possiblePathCount += 1

    # 세로
    for j in range(N):
        isValidPath = True
        isRunwayPut = [False]*N

        for i in range(N-1):
            c, n = heights[i][j], heights[i+1][j]

            # 같을 경우
            if c == n:
                continue

            # 1 2
            elif c+1 == n:
                flag = True

                # 경사로 놓기
                for k in range(i-L+1, i+1):
                    if k < 0 or heights[k][j] != c or isRunwayPut[k] == True:
                        flag = False
                        break
                    else:
                        isRunwayPut[k] = True

                # 경사로 놓기에 실패
                if not flag:
                    isValidPath = False
                    break
            # 2 1
            elif c == n+1:
                flag = True

                # 경사로 놓기
                for k in range(i+1, i+L+1):
                    if k > N-1 or heights[k][j] != n or isRunwayPut[k] == True:
                        flag = False
                        break
                    else:
                        isRunwayPut[k] = True

                # 경사로 놓기에 실패
                if not flag:
                    isValidPath = False
                    break

            # 높이 차이가 2 이상
            else:
                isValidPath = False
                break
        if isValidPath:
            possiblePathCount += 1

    return possiblePathCount


if __name__ == '__main__':
    N, L = map(int, input().split())
    heights = [list(map(int, input().split())) for _ in range(N)]

    possiblePathCount = getPossiblePathCount()
    print(possiblePathCount)
