# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
FALSE, TRUE, UNKNOWN = 0, 1, 2
  
def f():             
  cur_status = [UNKNOWN]*10
  for a, b in opinions:
    # 모순
    if(cur_status[b] != UNKNOWN and cur_status[b] != a):
      return

    cur_status[b] = a     
       
  # Set counts
  false_count = 0
  true_count = 0
  true_index = 0
  unknown_count = 0
             
  for i in range(1, 10):
    if(cur_status[i] == TRUE):    
      true_count += 1
      true_index = i
    elif(cur_status[i] == FALSE):
      false_count += 1 
    else: # UNKNOWN
      unknown_count += 1

  # Set status
  if(true_count == 1):
    status[true_index] = TRUE
  elif(true_count == 0):
    for i in range(1, 10):
      if(cur_status[i] == UNKNOWN):
        status[i] = TRUE        

def get_unique_true_index():
  res = -1
  for i in range(1, 10):
    if(status[i] == TRUE):
      # 여러 명이 1루수
      if(res != -1):
        res = -1
        break

      res = i

  return res

if __name__ == '__main__':
  opinions = [list(map(int, input().split())) for _ in range(9)]      

  status = [FALSE]*10
  for i in range(9):
    opinions[i][0] = (opinions[i][0] + 1) % 2
    f()                               
    opinions[i][0] = (opinions[i][0] + 1) % 2
  
  print(get_unique_true_index())