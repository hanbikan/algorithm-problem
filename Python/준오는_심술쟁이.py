# -*- coding: utf-8 -*-
import sys                           
input = sys.stdin.readline       
INF = 1000000007
                           
if __name__ == '__main__':
  s = int(input())            
  n = len(str(input().rstrip()))      
                               
  dp = [0]*(s+1) # dp[k]: k만큼 바꿨을 때의 경우의 수
  dp[0] = 1
  next_dp = [0]*(s+1)

  for _ in range(n):                      
    prefix_sum = 0

    for k in range(s+1):     
      prefix_sum = (prefix_sum + dp[k]) % INF
      if k > 25: # 1 <= k <= 25(문제 조건)이므로 부분합의 범위를 조절해줌
        prefix_sum = (prefix_sum - dp[k-26] + INF) % INF

      next_dp[k] = prefix_sum

    # dp에 next_dp값을 가리키게 하기 위해 포인터를 스왑해준다.
    # 어차피 next_dp는 초기값에 상관없이 갱신되므로 dp를 가져도 상관 없다.
    dp, next_dp = next_dp, dp

  print(dp[-1])