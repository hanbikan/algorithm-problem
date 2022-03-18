# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

if __name__ == '__main__':
  # 시작/끝/6개의 텔레포트 지점 ... 총 8개를 노드화
  positions = [list(map(int, input().split())) for _ in range(2)]
  dists = [[float('inf')]*8 for _ in range(8)]    
                                            
  for n in range(2, 8, 2): # 2-3/4-5/6-7
    x1, y1, x2, y2 = map(int, input().split()) 
    positions.append([x1,y1])
    positions.append([x2,y2])

    dists[n][n+1] = 10                  
    dists[n+1][n] = 10                  
                   
  for i in range(8):
    for j in range(i, 8):
      diff = abs(positions[i][0] - positions[j][0]) + abs(positions[i][1] - positions[j][1])
      
      # 텔레포트보다 점프가 더 빠를 수도 있음
      dists[i][j] = min(dists[i][j], diff)
      dists[j][i] = min(dists[j][i], diff)

  # 플로이드 와샬
  for k in range(8):
    for i in range(8):
      for j in range(8):
        if dists[i][j] > dists[i][k] + dists[k][j]:
          dists[i][j] = dists[i][k] + dists[k][j]
  print(dists[0][1])