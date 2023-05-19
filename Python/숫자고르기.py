import sys
input = sys.stdin.readline

def dfs(node, stack: list):
    for next_node in graph[node]:
        if next_node > N: continue
        if visited_at[next_node] != -1:
            if next_node not in stack: continue
            for i in range(len(stack) - 1, -1, -1):
                result.add(stack[i])
                if stack[i] == next_node: break
        else:
            visited_at[next_node] = visited_at[node] + 1
            stack.append(next_node)
            dfs(next_node, stack)
            stack.pop()

N = int(input())
graph = {i:[] for i in range(1, N + 1)}
for i in range(1, N + 1):
    num = int(input())
    graph[i].append(num)

result = set()
visited_at = [-1] * (N + 1)
for i in range(1, N + 1):
    if visited_at[i] == -1:
        visited_at[i] = 0
        dfs(i, [i])
sorted_result = sorted(list(result))
print(len(sorted_result))
for i in range(len(sorted_result)):
    print(sorted_result[i])