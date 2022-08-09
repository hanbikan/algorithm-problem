import sys
input = sys.stdin.readline

def f(left, index, current_sum):
  if(left == 0):
    return current_sum
  
  res = 0
  for i in range(index, N-left+1):
    cur_res = f(left - 1, i+1, current_sum + cards[i])
    if cur_res <= M:
      res = max(res, cur_res)

  return res

if __name__ == '__main__':
  N, M = map(int, input().split())        
  cards = list(map(int, input().split()))

  print(f(3, 0, 0))