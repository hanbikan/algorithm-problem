import sys
input = sys.stdin.readline

def get_score(node):
    is_visited = [False] * (N + 1)
    is_visited[node] = True
    current_level = 0
    q = [node]

    while (len(q) > 0):
        nq = []
        while (len(q) > 0):
            cur = q.pop()
            for nxt in graph[cur]:
                if (not is_visited[nxt]):
                    is_visited[nxt] = True
                    nq.append(nxt)
        q = nq
        current_level += 1
    current_level -= 1

    return current_level

N = int(input())
graph = {i: [] for i in range(1, N + 1)}
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

min_score = float('inf')
scores = [0]
for i in range(1, N + 1):
    scores.append(get_score(i))
    min_score = min(min_score, scores[-1])

candidates = []
for i in range(1, N + 1):
    if scores[i] == min_score:
        candidates.append(i)

print(min_score, len(candidates))
print(*candidates)