# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def get_distance(x1, y1, x2, y2):
  return abs(x1 - x2) + abs(y1 - y2) - 1

def dfs(x, y, continent_index):
  global mp
  res = []                

  # 바다와 인접해있다면 현재 위치 추가
  for k in range(4):
    nx, ny = x + dx[k], y + dy[k]    
    if not (0 <= nx <= N-1 and 0 <= ny <= N-1): continue
    if mp[nx][ny] == 0:
      res.append([x,y])
      break

  # DFS
  for k in range(4):
    nx, ny = x + dx[k], y + dy[k]     
    
    if not (0 <= nx <= N-1 and 0 <= ny <= N-1): continue
    if not (mp[nx][ny] == 1): continue   
    
    mp[nx][ny] = continent_index
    res += dfs(nx, ny, continent_index)

  return res

def get_shortest_distance(continent_index1, continent_index2):
  res = float('inf')

  for x1, y1 in continent_to_outlines[continent_index1]:
    for x2, y2 in continent_to_outlines[continent_index2]:            
      res = min(res, get_distance(x1, y1, x2, y2))          

  return res

if __name__ == '__main__':
  N = int(input())
  mp = [list(map(int, input().split())) for _ in range(N)]

  continent_index = 2
  continent_to_outlines = {}
  for i in range(N):
    for j in range(N):
      if mp[i][j] == 1:
        # mp에 continent_index로 색칠 + outlines 가져오기
        mp[i][j] = continent_index
        continent_to_outlines[continent_index] = dfs(i, j, continent_index)
        continent_index += 1

  # 대륙 to 대륙 ... 모든 outlines에 대해 거리를 계산하여 최소값 구하기
  res = float('inf')
  for i in range(2, continent_index):
    for j in range(i+1, continent_index):          
      res = min(res, get_shortest_distance(i, j))   

  print(res)