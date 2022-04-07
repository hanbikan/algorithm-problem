import sys, math, decimal
input = sys.stdin.readline

if __name__ == '__main__':
  N, K = map(int, input().split())
  v = list(map(int, input().split()))     
  v.sort()

  max_speed = 0
  for second_start in range(1, N):
    first_length = second_start
    second_length = N - second_start

    max_speed = max(
      max_speed,
      v[0]*first_length + v[second_start]*second_length 
    )                                 

  print(math.ceil(decimal.Decimal(K) / decimal.Decimal(max_speed)))