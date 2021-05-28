import sys
input = sys.stdin.readline

N = int(input())
scores = [int(input()) for _ in range(N)]
scores.sort()
sum = sum([abs(scores[i]-(i+1)) for i in range(N)])

print(sum)
