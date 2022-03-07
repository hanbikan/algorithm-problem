import sys
input = sys.stdin.readline
    
def get_diff(start_x, end_x, start_y, end_y):
  res1 = 0
  for x in range(start_x, end_x+1):
    for y in range(start_y, end_y+1):
      res1 += is_wrong1[x][y]
  
  res2 = 0
  for x in range(start_x, end_x+1):
    for y in range(start_y, end_y+1):
      res2 += is_wrong2[x][y]

  return min(res1, res2)

if __name__ == '__main__':
  N, M = map(int,input().split())
  board = [str(input().rstrip()) for _ in range(N)]

  is_wrong1 = [[0]*M for _ in range(N)]
  comparison_target1 = ['WB', 'BW'] 
  for i in range(N):
    for j in range(M):
      if board[i][j] != comparison_target1[i%2][j%2]:
        is_wrong1[i][j] = 1

  is_wrong2 = [[0]*M for _ in range(N)]    
  comparison_target2 = ['BW', 'WB'] 
  for i in range(N):
    for j in range(M):
      if board[i][j] != comparison_target2[i%2][j%2]:
        is_wrong2[i][j] = 1

  
  res = float('inf')
  for start_x in range(0, N-7):
    end_x = start_x + 7
    for start_y in range(0, M-7):
      end_y = start_y + 7
      res = min(res, get_diff(start_x, end_x, start_y, end_y))
  print(res)