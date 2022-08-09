# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline   

X_LENGTH, Y_LENGTH = 65, 89
DX, DY = 0, 1     
d = [
  [[-1,-1,2],[-2,2,0]], # Y 모양
  [[-2,1,1],[0,-2,2]] # ㅗ 모양
] # d[phase][DX][k]
                      
def convert_x(x):
  return X_LENGTH//2 + x  

def convert_y(y):
  return Y_LENGTH//2 + y  

def f(remaining_count, x, y, px, py, phase):    
  if remaining_count == 0:
    return 0

  global is_visited
  res = 0

  for k in range(3):
    nx, ny = x + d[phase][DX][k], y + d[phase][DY][k]
    
    if is_visited[nx][ny]:
      if remaining_count == 1 and not (nx == px and ny == py):
        res += 1
      continue

    is_visited[nx][ny] = True
    res += f(remaining_count-1, nx, ny, x, y, (phase+1)%2)   
    is_visited[nx][ny] = False

  return res

if __name__ == '__main__':
  N = int(input())    
                                      
  if N < 5:
    res = 0
  elif 5 <= N <= 6:
    res = 2
  elif N == 7:
    res = 4
  else:          
    is_visited = [[False]*Y_LENGTH for _ in range(X_LENGTH)]    
    is_visited[convert_x(0)][convert_y(0)] = True
    is_visited[convert_x(-2)][convert_y(0)] = True
    is_visited[convert_x(-3)][convert_y(-2)] = True
    res = f(N-1, convert_x(-3), convert_y(-2), convert_x(-2), convert_y(0), 1)*2

  print(res)                  