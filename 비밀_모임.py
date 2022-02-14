import sys                        
input = sys.stdin.readline  
INF = 100001

if __name__ == '__main__':
  for _ in range(int(input())):
    # Input
    N, M = map(int, input().split())   
    
    dists = [[INF]*(N+1) for _ in range(N+1)]
    for _ in range(M):
      a, b, c = map(int, input().split())
      dists[a][b] = c
      dists[b][a] = c 
      
    int(input()) # K
    rooms = list(map(int, input().split()))


    # Floyd-Warshall
    for k in range(1, N+1):
      dists[k][k] = 0
      for i in range(1, N+1):
        for j in range(1, N+1):
          dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])


    # Print minDistNode
    minDistSum = float('inf')
    minDistNode = 0

    for i in range(1, N+1):
      distSum = sum(dists[room][i] for room in rooms)
      if minDistSum > distSum:
        minDistSum = distSum
        minDistNode = i

    print(minDistNode)