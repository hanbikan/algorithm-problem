# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

DOWN, UP, RIGHT, LEFT = 0,1,2,3
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def encode_position(x, y):
  return x*M + y

def decode_position(n):
  return [n//M, n%M]
           
def tlit(direction):
  # 두 구슬이 어디로 가야할지 정함
  next_red_pos = [red_pos[0],red_pos[1]]
  next_blue_pos = [blue_pos[0],blue_pos[1]]

  while True:
    nx, ny = next_red_pos[0] + dx[direction], next_red_pos[1] + dy[direction]
    if mapp[nx][ny] == '#' or mapp[next_red_pos[0]][next_red_pos[1]] == 'O':
      break
    next_red_pos[0], next_red_pos[1] = nx, ny

  while True:
    nx, ny = next_blue_pos[0] + dx[direction], next_blue_pos[1] + dy[direction]
    if mapp[nx][ny] == '#' or mapp[next_blue_pos[0]][next_blue_pos[1]] == 'O':
      break
    next_blue_pos[0], next_blue_pos[1] = nx, ny


  # 겹칠 경우
  if next_red_pos[0] == next_blue_pos[0] and next_red_pos[1] == next_blue_pos[1]:
    # 예외: 두 구슬이 모두 구멍에 들어감
    if hole_pos[0] == next_red_pos[0] and hole_pos[1] == next_red_pos[1]:
      return False

    if direction == DOWN:
      if red_pos[0] > blue_pos[0]:
        next_blue_pos[0] -= dx[direction]
      else:               
        next_red_pos[0] -= dx[direction]
    elif direction == UP:   
      if red_pos[0] > blue_pos[0]:
        next_red_pos[0] -= dx[direction]
      else:               
        next_blue_pos[0] -= dx[direction]
    elif direction == RIGHT:            
      if red_pos[1] > blue_pos[1]:
        next_blue_pos[1] -= dy[direction]
      else:               
        next_red_pos[1] -= dy[direction]
    else:    
      if red_pos[1] > blue_pos[1]:
        next_red_pos[1] -= dy[direction]
      else:               
        next_blue_pos[1] -= dy[direction]
  
  # 계산된 두 좌표를 실제로 적용
  apply(red_pos, blue_pos, next_red_pos, next_blue_pos)
  
  return True

def apply(prev_red_pos, prev_blue_pos, next_red_pos, next_blue_pos):
  global mapp, red_pos, blue_pos

  # 실제 맵에 대입
  prev_red_value = mapp[prev_red_pos[0]][prev_red_pos[1]]
  mapp[prev_red_pos[0]][prev_red_pos[1]] = mapp[next_red_pos[0]][next_red_pos[1]]        
  mapp[next_red_pos[0]][next_red_pos[1]] = prev_red_value     

  prev_blue_value = mapp[prev_blue_pos[0]][prev_blue_pos[1]]
  mapp[prev_blue_pos[0]][prev_blue_pos[1]] = mapp[next_blue_pos[0]][next_blue_pos[1]]
  mapp[next_blue_pos[0]][next_blue_pos[1]] = prev_blue_value

  # 실제 좌표에 대입
  red_pos = [next_red_pos[0],next_red_pos[1]]  
  blue_pos = [next_blue_pos[0],next_blue_pos[1]]    

def dfs(count):
  global dp       
                                                                   
  if hole_pos[0] == red_pos[0] and hole_pos[1] == red_pos[1]:                      
    return count                                                    
  if hole_pos[0] == blue_pos[0] and hole_pos[1] == blue_pos[1]:                      
    return float('inf')

  res = float('inf')

  for k in range(4):             
    # 백트래킹을 위해 미리 저장해둠
    prev_red_pos = [red_pos[0], red_pos[1]]
    prev_blue_pos = [blue_pos[0], blue_pos[1]]

    if not tlit(k): # 두 구슬이 모두 구멍에 들어간 경우
      continue            

    r, b = encode_position(*red_pos), encode_position(*blue_pos)
    if dp[r][b] > count + 1:
      dp[r][b] = count + 1
      res = min(res, dfs(count + 1))
              
    # 백트래킹
    apply(red_pos, blue_pos, prev_red_pos, prev_blue_pos)      

  return res


if __name__ == '__main__':
  N, M = map(int, input().split())
  mapp = [[c for c in input().rstrip()] for _ in range(N)]
                
  red_pos = [-1,-1]
  blue_pos = [-1,-1]
  hole_pos = [-1,-1]              
  for i in range(N):
    for j in range(M):         
      if mapp[i][j] == 'R':
        red_pos = [i,j]      
      if mapp[i][j] == 'B':
        blue_pos = [i,j]    
      if mapp[i][j] == 'O':
        hole_pos = [i,j] 
                   
  # dp[R][B]: 빨간 구슬이 R, 파란 구슬이 B에 있을 때의 도달 카운트
  dp = [[float('inf')]*(N*M) for _ in range(N*M)]      
  dp[encode_position(*red_pos)][encode_position(*blue_pos)] = 0
  
  res = dfs(0)
  if res == float('inf'):
    print(-1)
  else:
    print(res)