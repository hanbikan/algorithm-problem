import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []

M = int(input())

for _ in range(M):
    curLine = list(map(str, input().rstrip().split()))

    if curLine[0] == 'L' and left:
        right.append(left.pop())
    elif curLine[0] == 'D' and right:
        left.append(right.pop())
    elif curLine[0] == 'B' and left:
        left.pop()
    elif curLine[0] == 'P':
        left.append(curLine[1])

print("".join(left)+"".join(reversed(right)))
