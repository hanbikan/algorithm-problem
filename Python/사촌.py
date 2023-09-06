import sys
input = sys.stdin.readline

while True:
    n, k = map(int, input().split())
    if n == k == 0:
        break
    nums = list(map(int, input().split()))
    if k == nums[0]:
        print(0)
    else:
        graph = {nums[i]: [] for i in range(n)}
        current_level_nodes = [nums[0]]
        parent_level_nodes = []
        current_parent_index = 0
        for i in range(1, n):
            prev, cur = nums[i - 1], nums[i]
            if prev + 1 != cur:
                if i == 1 or current_parent_index + 1 == len(parent_level_nodes):
                    current_parent_index = 0
                    parent_level_nodes = [current_level_nodes[i] for i in range(len(current_level_nodes))]
                    current_level_nodes = []
                else:
                    current_parent_index += 1
            current_level_nodes.append(cur)
            parent = parent_level_nodes[current_parent_index]
            graph[parent].append(cur)
            graph[cur].append(parent)

        parent = graph[k][0]
        if parent == nums[0]:
            print(0)
        else:
            grand_parent = graph[parent][0]
            q = [grand_parent]
            for _ in range(2):
                nq = []
                while len(q) > 0:
                    cur = q.pop(0)
                    start_index = 1 if cur != nums[0] else 0
                    for i in range(start_index, len(graph[cur])):
                        nxt = graph[cur][i]
                        if nxt == parent:continue
                        nq.append(nxt)
                q = nq
            print(len(q))