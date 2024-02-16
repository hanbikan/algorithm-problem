import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(node):
    for next_node in graph[node]:
        if next_node in visited:
            continue
        visited.add(next_node)
        dfs(next_node)

def get_start_node_of_rod(node):
    if len(backward_graph[node]) == 0 and len(graph[node]) == 1:
        return node
    for next_node in backward_graph[node]:
        if next_node in visited: continue
        visited.add(next_node)
        next_res = get_start_node_of_rod(next_node)
        if next_res:
            return next_res
    return None

def is_donut(node):
    if len(graph[node]) != 1: return False

    for next_node in graph[node]:
        if next_node in visited:
            return True
        visited.add(next_node)
        if is_donut(next_node): return True
    return False

def is_rod(node):
    if len(graph[node]) >= 2: return False

    for next_node in graph[node]:
        if next_node in visited:
            return False
        visited.add(next_node)
        if not is_rod(next_node): return False
    return True

def get_circle_length(node, length):
    res = float('inf')
    for next_node in graph[node]:
        if next_node in visited_for_circle_length:
            return length
        visited_for_circle_length.add(next_node)
        res = min(get_circle_length(next_node, length + 1), res)
    return res

def is_eight_shaped_recur(node, size):
    global visited_for_circle_length
    if size == 0: return False

    if len(graph[node]) >= 3:
        return False
    elif len(graph[node]) == 2:
        visited_for_circle_length = set()
        visited_for_circle_length.add(graph[node][0])
        l1 = get_circle_length(graph[node][0], 0)
        visited_for_circle_length = set()
        visited_for_circle_length.add(graph[node][1])
        l2 = get_circle_length(graph[node][1], 0)
        return l1 == l2 == size
    else:
        for next_node in graph[node]:
            if next_node in visited: continue
            visited.add(next_node)
            if not is_eight_shaped_recur(next_node, size):
                return False
        return True

def is_eight_shaped(node):
    global visited_for_circle_length
    visited_for_circle_length = set()
    visited_for_circle_length.add(node)
    circle_length = get_circle_length(node, 0)
    return is_eight_shaped_recur(node, circle_length)

def get_graph_index(node):
    global visited

    visited = set()
    visited.add(node)
    if is_donut(node):
        return 0

    if len(backward_graph[node]) == 2:
        visited = set()
        visited.add(node)
        start_node = get_start_node_of_rod(node)
        if start_node:
            visited = set()
            visited.add(start_node)
            if is_rod(start_node):
                return 1
    elif len(backward_graph[node]) == 1:
        visited = set()
        visited.add(node)
        if is_rod(node):
            return 1

    visited = set()
    visited.add(node)
    if is_eight_shaped(node):
        visited = set()
        visited.add(node)
        dfs(node)
        return 2
    
    return -1

def solution(edges):
    global graph, backward_graph, visited_overall
    graph = {}
    backward_graph = {}
    nodes = set()
    for fr, to in edges:
        nodes.add(fr)
        nodes.add(to)
        if graph.get(fr):
            graph[fr].append(to)
        else:
            graph[fr] = [to]
        if backward_graph.get(to):
            backward_graph[to].append(fr)
        else:
            backward_graph[to] = [fr]
    nodes = list(nodes)
    n = len(nodes)

    for node in nodes:
        if not graph.get(node): graph[node] = []
        if not backward_graph.get(node): backward_graph[node] = []
    
    # Check
    nodes_without_backwards = []
    for node in nodes:
        if len(backward_graph[node]) == 0:
            nodes_without_backwards.append(node)

    for node in nodes_without_backwards:
        flag = True
        counts = [0, 0, 0]
        visited_overall = set()
        for adj_node in graph[node]:
            if adj_node == node: continue
            adj_graph_index = get_graph_index(adj_node)
            if adj_graph_index == -1:
                flag = False
                break
            visited_overall = visited_overall.union(visited)
            counts[adj_graph_index] += 1
        if flag and len(visited_overall) == n - 1 and not node in visited_overall:
            return [node] + counts

res = solution(
    #[[2,3],[4,3],[1,1],[2,1]]
    [[4,11],[1,12],[8,3],[12,7],[4,2],[7,11],[4,8],[9,6],[10,11],[6,10],[3,5],[11,1],[5,3],[11,9],[3,8]]
)
print(res)