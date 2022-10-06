import sys
input = sys.stdin.readline

def f(cur_node, dest, cur_str):
    global result
    if cur_node == dest:
        result = cur_str
        return True

    res = None
    for next_node in graph[cur_node]:
        if is_visited[next_node]: continue

        cur_str.append(strr[next_node])
        is_visited[next_node] = True
        if f(next_node, dest, cur_str): return
        is_visited[next_node] = False
        cur_str.pop()

def main():
    global graph,strr, is_visited, result

    N = int(input())
    strr = ['0'] + [str(input().rstrip()) for _ in range(N)]

    graph = {i:[] for i in range(1,N+1)}
    for _ in range(N-1):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
        is_visited = [False]*(N+1)
    for _ in range(int(input())):
        a,b,c,d = map(int,input().split())
        
        is_visited[a] = True
        f(a, b, [strr[a]])
        is_visited[a] = False
        res1 = result

        is_visited[c] = True
        f(c, d, [strr[c]])
        is_visited[c] = False
        res2 = result

        count = 0
        for i in range(len(res1)):
            cur = res1[i]
            for j in range(len(res2)):
                if cur == res2[j]:
                    count += 1
                    break
        print(count)

if __name__=="__main__":
    main()