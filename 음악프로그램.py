import sys
input = sys.stdin.readline


def solution():
    # input / set childs
    childs = [[] for _ in range(N+1)]

    for _ in range(M):
        curNums = list(map(int, input().split()))
        curLen = curNums[0]

        if curLen >= 2:
            for i in range(1, curLen):
                p, c = curNums[i], curNums[i+1]
                childs[p].append(c)

    # set entryLevels
    entryLevels = [0]*(N+1)
    for i in range(1, N+1):
        for c in childs[i]:
            entryLevels[c] += 1

    # initialize queue
    queue = []
    for i in range(1, N+1):
        if entryLevels[i] == 0:
            queue.append(i)

    # set toPrint
    toPrint = []
    while queue:
        cur = queue.pop(0)
        toPrint.append(cur)

        for c in childs[cur]:
            entryLevels[c] -= 1

            if entryLevels[c] == 0:
                queue.append(c)

    # print
    if len(toPrint) == N:
        for n in toPrint:
            print(n)
    else:
        print(0)


if __name__ == '__main__':
    N, M = map(int, input().split())

    solution()
