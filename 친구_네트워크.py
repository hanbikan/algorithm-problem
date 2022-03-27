import sys
input = sys.stdin.readline

def find(x):
  if parents[x] == x:
    return parents[x]
                             
  parents[x] = find(parents[x])   
  return parents[x]

def union(x, y):
  px, py = find(x), find(y)      

  if px < py:
    parents[py] = px     
    counts[px] += counts[py]
    return counts[px]
  elif px > py:                  
    parents[px] = py    
    counts[py] += counts[px]  
    return counts[py]
  else:
    return counts[px]

if __name__ == '__main__':
  for _ in range(int(input())):
    F = int(input())

    index_count = 0
    name_to_index = {}

    inputs = [list(map(str, input().rstrip().split())) for _ in range(F)]
    for i in range(F):
      a, b = inputs[i]

      if not name_to_index.get(a):
        name_to_index[a] = index_count
        index_count += 1
      
      if not name_to_index.get(b):
        name_to_index[b] = index_count
        index_count += 1
                      
    parents = [i for i in range(index_count)]    
    counts = [1 for _ in range(index_count)]    
    for i in range(F):    
      a, b = inputs[i]
      a_index, b_index = name_to_index[a], name_to_index[b]

      print(union(a_index, b_index))        