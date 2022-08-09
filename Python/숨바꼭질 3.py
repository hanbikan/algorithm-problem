import sys
input = sys.stdin.readline


def getMinTimeToCatch(N, K):
    todo = [(N, 0)]
    isVisited = [False]*100001
    isVisited[N] = True

    while todo:
        x, t = todo.pop(0)
        isVisited[x] = True

        if x == K:
            break

        if x-1 >= 0 and isVisited[x-1] == False:
            todo.append((x-1, t+1))
        if x+1 <= 100000 and isVisited[x+1] == False:
            todo.append((x+1, t+1))
        if x*2 <= 100000 and isVisited[x*2] == False:
            todo.insert(0, (x*2, t))

    return t


if __name__ == '__main__':
    N, K = map(int, input().split())

    minTimeToCatch = getMinTimeToCatch(N, K)
    print(minTimeToCatch)
