import sys
input = sys.stdin.readline

def get_adjacent_indexes(index):
    i1 = (index+N)%(2*N)
    i2 = index+1
    if(i2 % N == 0): i2 -= N
    i3 = index-1
    if(index % N == 0): i3 += N
    return i1,i2,i3

def get_info(index):
    return info[index//N][index%N]

def f(index, should_merge):
    is_visited[index] = True
    
    res = 1 if should_merge else 0
    if not should_merge:
        for n in graph[index]:
            if not is_visited[n]:
                res += f(n, True)
    else:
        start = len(graph[index])
        for i in range(len(graph[index])):
            n = graph[index][i]
            if not is_visited[n]:
                res += f(n, False)
                start = i+1
                break
        for i in range(start, len(graph[index])):
            n = graph[index][i]
            if not is_visited[n]:
                res += f(n, True)
    return res

if __name__ == "__main__":
    for _ in range(int(input())):
        N, W = map(int,input().split())
        info = [list(map(int,input().split())) for _ in range(2)]

        graph = {i:[] for i in range(2*N)}
        for i in range(2):
            for j in range(N):
                cur = info[i][j]
                for index in get_adjacent_indexes(i*N + j):
                    if(cur + get_info(index) <= W):
                        graph[i*N + j].append(index)
        
        res = 0
        is_visited = [False]*(2*N)
        for i in range(2*N):
            if not is_visited[i]:
                res += f(i, True)

        print(res)