# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

def dfs(node, direction):
  res = 1
  for nxt in graph[direction][node]:
    if(not is_visited[nxt]):   
      is_visited[nxt] = True
      res += dfs(nxt, direction)        

  return res
          
if __name__ == '__main__':
  N = int(input())
  M = int(input())

  graph = [{i:[] for i in range(1, N+1)} for _ in range(2)]
  for _ in range(M):
    h, l = map(int, input().split())
    # 방향을 달리하여 따로 저장한다.
    graph[0][h].append(l)    
    graph[1][l].append(h)  
    
  for i in range(1, N+1):
    # 각 방향별로 탐색을 따로 한다.
    is_visited = [False]*(N+1)
    res1 = dfs(i, 0)-1

    is_visited = [False]*(N+1)
    res2 = dfs(i, 1)-1

    print(N - (res1 + res2 + 1))