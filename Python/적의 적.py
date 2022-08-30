import sys
input = sys.stdin.readline

def bfs(start_node):
    global colors

    q = [start_node]
    colors[start_node] = 0

    while len(q) > 0:
        cur_node = q.pop(0)

        for next_node in graph[cur_node]:
            if colors[next_node] != -1:
                if colors[cur_node] == colors[next_node]:
                    return False
            else:
                q.append(next_node)
                colors[next_node] = (colors[cur_node] + 1) % 2
            
    return True

N, M = map(int,input().split())
graph = {i: set() for i in range(1, N+1)}

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)

result = True
colors = [-1]*(N+1)
for i in range(1, N+1):
    if colors[i] == -1 and bfs(i) == False:
        result = False

print(int(result))