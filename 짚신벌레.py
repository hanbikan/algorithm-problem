# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
DIV = 1000

if __name__ == '__main__':
  a, b, d, N = map(int, input().split())

  dp = [0]*(N+1)
  dp[0] = 1

  prefix_sum = 0
  for i in range(1, N+1):    
    prefix_sum = (prefix_sum + dp[i-a] - dp[i-b] + DIV) % DIV
    dp[i] = prefix_sum    
    
  sm = 0
  for i in range(max(0, N-d+1), N+1):
    sm = (sm + dp[i]) % DIV
  print(sm)