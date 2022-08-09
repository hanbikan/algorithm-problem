import sys
input = sys.stdin.readline

N = int(input())
scores = sorted([int(input()) for _ in range(N)])

print(sum(abs(scores[i]-(i+1)) for i in range(N)))
