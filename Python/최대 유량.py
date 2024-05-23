import sys, collections

input = sys.stdin.readline
LEN = 26 * 2

def alphabet_to_num(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    else:
        return ord(c) - ord('a') + 26

def get_maximum_flow(src, dst):
    total_flow = 0
    flow = [[0] * LEN for _ in range(LEN)]

    while True:
        parent = [-1] * LEN
        parent[src] = src
        q = collections.deque([src])

        while q and parent[dst] == -1:
            cur_node = q.popleft()

            for next_node in range(LEN):
                if capacity[cur_node][next_node] - flow[cur_node][next_node] > 0 and parent[next_node] == -1:
                    q.append(next_node)
                    parent[next_node] = cur_node

        if parent[dst] == -1:
            break

        amount = float('inf')
        c = dst
        while c != src:
            amount = min(amount, capacity[parent[c]][c] - flow[parent[c]][c])
            c = parent[c]

        c = dst
        while c != src:
            flow[parent[c]][c] += amount
            flow[c][parent[c]] -= amount
            c = parent[c]
        total_flow += amount

    return total_flow

N = int(input())
capacity = [[0] * LEN for _ in range(LEN)]
is_visited = [False] * LEN
for _ in range(N):
    a, b, c = map(str, input().split())
    a, b = alphabet_to_num(a), alphabet_to_num(b)
    c = int(c)
    capacity[a][b] += c
    capacity[b][a] += c

print(get_maximum_flow(alphabet_to_num('A'), alphabet_to_num('Z')))
