# -*- coding: utf-8 -*-
import sys, math
input = sys.stdin.readline
INF = 10001

def convert_point_to_index(x, y):
  return INF*x + y

def convert_index_to_point(index):
  return index//INF, index%INF

def get_area(x1, y1, x2, y2):
  return math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)

def solution():
  max_area = 0
  for index in points:                   
    max_area = max(max_area, get_max_area_at(*convert_index_to_point(index)))
    
  return int(max_area)

def get_max_area_at(x, y):
  res = 0
  for index in points:
    adj_x, adj_y = convert_index_to_point(index)

    offset_x, offset_y = adj_x - x, adj_y - y
    cur_x, cur_y = adj_x, adj_y      

    # (x,y) - (adj_x,adj_y) 직선을 포함하는 정사각형 찾기
    for _ in range(2):
      offset_x, offset_y = offset_y, -offset_x
      cur_x, cur_y = cur_x + offset_x, cur_y + offset_y     

      if(convert_point_to_index(cur_x, cur_y) not in points):
        break         
    else:                                                         
      res = max(res, get_area(x, y, adj_x, adj_y))

  return res
                                           
if __name__ == '__main__':
  for _ in range(int(input())):     
    points = {convert_point_to_index(*map(int, input().split())) for _ in range(int(input()))}                                    
    print(solution()) 