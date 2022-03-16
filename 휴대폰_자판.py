# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
                          
class Node:
  def __init__(self, c):
    self.c = c
    self.childrens = {}
    self.count = 0
    self.is_end = False

class Trie:
  def __init__(self):
    self.root = Node('R')

  def insert(self, strr):
    cur = self.root

    for c in strr:     
      # 없을 경우 새로 추가해줌
      if not cur.childrens.get(c):   
        cur.childrens[c] = Node(c)  
      
      cur = cur.childrens[c]     
      cur.count += 1

    cur.is_end = True

  def dfs(self, node, type_count):
    if node.count == 1:
      # 현재까지 입력한 횟수를 더하되 더이상 탐색을 해선 안 된다.
      return type_count

    res = 0
    if node.is_end:
      # 이 조건문을 통과했다는 것은, node.count가 1보다 크면서 이 노드가
      # 한 단어의 마지막이라는 것이므로, 횟수를 더하되 탐색은 계속한다.
      res += type_count     

    for next_node in node.childrens.values():     
      # 현재 노드의 카운트와 다음 노드의 카운트가 같다는 것은, 입력 가능한
      # 다른 문자가 없다는 것이므로 카운트하지 않는다.(자동 입력)
      if node.count == next_node.count:
        next_type_count = type_count
      else:
        next_type_count = type_count + 1

      res += self.dfs(next_node, next_type_count)

    return res

if __name__ == '__main__':
  while True:
    try:
      N = int(input())  
    except:
      break

    trie = Trie()    
    for _ in range(N):               
      trie.insert(str(input().rstrip()))

    print('%0.2f' % (trie.dfs(trie.root, 0) / N))
    