import sys
input = sys.stdin.readline

N = int(input())
queue = []

for _ in range(N):
    curLine = list(map(str, input().split()))
    operator = curLine[0]

    if operator == 'push':
        queue.append(int(curLine[1]))
    elif operator == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif operator == 'size':
        print(len(queue))
    elif operator == 'empty':
        print(int(len(queue) == 0))
    elif operator == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif operator == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
