import sys, math
input = sys.stdin.readline

def find_max_dist_with_index():
    max_dist = 0
    max_dist_index = 0
    last_visited = 0
    for i in range(len(positions)):
        p = positions[i]
        dist = math.ceil((p - last_visited) / (added[i] + 1))
        if dist > max_dist:
            max_dist = dist
            max_dist_index = i
        last_visited = p
    return (max_dist, max_dist_index)

N, M, L = map(int, input().split())
positions = list(map(int, input().split()))

# 82, 201, 411, 555, 622, 755, 800
positions.append(L)
positions.sort()
added = [0] * (N + 1)

for _ in range(M):
    _, max_dist_index = find_max_dist_with_index()
    added[max_dist_index] += 1

max_dist, _ = find_max_dist_with_index()
print(max_dist)