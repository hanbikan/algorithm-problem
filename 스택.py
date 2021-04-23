import sys
input = sys.stdin.readline

stack = []
N = int(input())
for _ in range(N):
    words = list(map(str, input().split()))
    if words[0] == 'push':
        stack.append(int(words[1]))
    elif words[0] == 'pop':
        if len(stack) >= 1:
            print(stack.pop())
        else:
            print(-1)
    elif words[0] == 'size':
        print(len(stack))
    elif words[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif words[0] == 'top':
        if len(stack) >= 1:
            print(stack[-1])
        else:
            print(-1)
