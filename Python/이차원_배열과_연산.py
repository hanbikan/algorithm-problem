# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
input = sys.stdin.readline

def get_sorted_list(nums):
  num_to_count = defaultdict(int)
  for num in nums:
    if num == 0: continue
    num_to_count[num] += 1
                                            
  num_to_count = list(num_to_count.items())   
  num_to_count.sort(key = lambda x:x[0])
  num_to_count.sort(key = lambda x:x[1])   
                                          
  return [num_to_count[i][j] for i in range(len(num_to_count)) for j in range(2)]
                             

if __name__ == '__main__':
  r, c, k = map(int, input().split())
  r -= 1
  c -= 1
  matrix = [list(map(int, input().split())) for _ in range(3)]
               
  for i in range(101):    
    width = len(matrix[0])
    height = len(matrix)    
    if r <= height-1 and c <= width-1 and matrix[r][c] == k:
      break

    # 한 줄씩 정렬해서 lines에 담음
    lines = []             
    next_width = 0
    next_height = 0
    if height >= width:
      next_height = height

      for i in range(height):
        lines.append(get_sorted_list(matrix[i]))
        next_width = max(next_width, len(lines[-1]))
    else:                          
      next_height = width

      for j in range(width):             
        lines.append(get_sorted_list(list(zip(*matrix))[j]))    
        next_width = max(next_width, len(lines[-1]))   

    # lines를 matrix에 적용
    matrix = [[0]*next_width for _ in range(next_height)]
    for i in range(next_height):
      for j in range(len(lines[i])):
        matrix[i][j] = lines[i][j]
                   
    # r < c일 경우 돌리기 
    if height < width:       
      matrix = list(zip(*matrix))    
      
    # 크기가 100을 넘길 경우 버리기  
    if next_width > 100:
      for i in range(next_height):
        matrix[i] = matrix[i][:100]
    if next_height > 100:
      matrix = matrix[:100]
  else:
    i = -1
      
  print(i)