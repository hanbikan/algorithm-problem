import sys
input = sys.stdin.readline

N = int(input())
homeworks = []
for _ in range(N):
    homeworks.append(list(map(int, input().split())))
homeworks.sort(reverse=True, key=lambda x: x[1])

score = 0
days = [0]*1001
for homework in homeworks:
    for d in range(homework[0], 0, -1):
        if days[d] == 0:
            days[d] = 1
            score += homework[1]
            break
print(score)
