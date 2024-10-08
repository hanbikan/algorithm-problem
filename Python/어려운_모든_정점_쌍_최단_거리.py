# -*- coding: utf-8 -*-
import sys                       
input = sys.stdin.readline
    
def find(n):
  if(parent[n] == n):
    return n
  else:
    return find(parent[n])

def union(n1, n2):
  p1 = find(n1)
  p2 = find(n2)

  if(p1 < p2):
    parent[p2] = parent[p1]
  else:
    parent[p1] = parent[p2]

def get_set_count(parent_var):
  res = 0
  for i in range(1, N+1):
    if(find(i) == parent_var):
      res += 1

  return res

if __name__ == '__main__':
  N, M, K = map(int, input().split())     
  
  parent = [i for i in range(N+1)]
  node1, node2 = None, None # 가중치가 1인 정점 쌍
  for i in range(M):
    u, v = map(int, input().split())
           
    if(i != K-1):
      union(u, v)
    else:
      node1, node2 = u, v

  if(find(node1) == find(node2)):
    print(0)
  else:
    count = get_set_count(parent[1])
    print(count * (N-count))