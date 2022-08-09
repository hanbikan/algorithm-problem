# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline       
KOOSAGA, CUBELOVER = 0, 1                   

if __name__ == '__main__':
  dp = [CUBELOVER]*1000001
  i = 1
  while(i*i < 1000001):
    dp[i*i] = KOOSAGA
    i += 1

  for i in range(2, 1000001):   
    if(dp[i] == CUBELOVER):  
      j = 1
      while(i + j*j < 1000001):
        dp[i + j*j] = KOOSAGA
        j += 1

  for _ in range(int(input())):
    N = int(input())
    if(dp[N] == KOOSAGA):
      print("koosaga")
    else:
      print("cubelover")