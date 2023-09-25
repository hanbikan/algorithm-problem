import sys
input = sys.stdin.readline

N = int(input())
dict = {1:1}
for i in range(2, N + 1):
    dict[i] = sum(dict.values())
    if i % 2 == 0:
        for j in range(i - 4, i - 2):
            if j <= 0: continue
            dict.pop(j)
print(sum(dict.values()))