import sys
input = sys.stdin.readline

N = int(input())

numbers = []
for _ in range(N):
    numbers.append(list(map(int, input().split())))

indices = [N-1]*N

for _ in range(N):
    maxNumber = numbers[indices[0]][0]
    maxIndex = 0
    for i in range(1, N):
        if maxNumber < numbers[indices[i]][i]:
            maxNumber = numbers[indices[i]][i]
            maxIndex = i

    indices[maxIndex] -= 1

indices[maxIndex] += 1
print(numbers[indices[maxIndex]][maxIndex])
