import sys
input = sys.stdin.readline
                            
if __name__ == '__main__':
    N, M = map(int, input().split())

    # 그래프 입력
    graph = [[0]*(N+1) for _ in range(N+1)]
    for i in range(1, N+1):      
        for j, num in enumerate(map(int, input().split())):               
            graph[i][j+1] = num

    # Floyd Warshall
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # 출력
    for _ in range(M):
       A, B, C = map(int, input().split())
       if(graph[A][B] <= C):
           print("Enjoy other party")
       else:
           print("Stay here")