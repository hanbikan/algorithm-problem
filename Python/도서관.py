import sys
input = sys.stdin.readline

N, M = map(int,input().split())
positions = list(map(int,input().split()))

positives = []
negatives = []
for pos in positions:
    if pos >= 0:
        positives.append(pos)
    else:
        negatives.append(pos)

positives.sort()
negatives.sort()
moves = []
for i in range(len(positives) - 1, -1, -M):
    moves.append(positives[i])
for i in range(0, len(negatives), M):
    moves.append(-negatives[i])

max_move = 0
for move in moves:
    if move > max_move:
        max_move = move
print(sum(moves) * 2 - max_move)