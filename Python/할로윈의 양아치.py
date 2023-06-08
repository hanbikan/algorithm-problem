import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(node):
    result_people, result_candies = 1, candies[node]

    for next_node in graph[node]:
        if is_visited[next_node]: continue

        is_visited[next_node] = True
        p, c = dfs(next_node)
        result_people += p
        result_candies += c
    
    return result_people, result_candies

N, M, K = map(int, input().split())
candies = [0] + list(map(int, input().split()))

graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS
is_visited = [False] * (N + 1)
people_and_candies = []
for i in range(1, N + 1):
    if not is_visited[i]:
        is_visited[i] = True
        p, c = dfs(i)
        people_and_candies.append([p, c])

# Knapsack: K = 6, [[2, 13], [4, 26], [2, 24], [2, 33]]
dp = [[0] * K for _ in range(len(people_and_candies) + 1)]
for i in range(1, len(people_and_candies) + 1):
    people, candies = people_and_candies[i - 1]
    for j in range(1, K):
        if j - people >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - people] + candies)
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])