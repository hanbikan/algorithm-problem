import sys, itertools
input = sys.stdin.readline
       
def is_same_string_pair(start_x, y1, y2):
  for i in range(start_x, R):
    if strs[i][y1] != strs[i][y2]:
      return False

  return True

def is_there_same_string_pair(x):
  c_to_y_indices = {} # row: aaba -> {'a':[0,1,3], 'b':[2]}         
  for j in range(C):
    c = strs[x][j]

    if c_to_y_indices.get(c):
      c_to_y_indices[c].append(j)
    else:
      c_to_y_indices[c] = [j]

  # Check if there is at least one same string pair
  for c, y_indices in c_to_y_indices.items():
    if len(y_indices) < 2: continue
                                      
    for y1, y2 in itertools.combinations(y_indices, 2):
      if is_same_string_pair(x+1, y1, y2):
        return True

  return False  

def find_biggest_index_with_no_same_string():          
  top, bottom = 1, R-1
  while top <= bottom:
    mid = (top + bottom)//2

    if is_there_same_string_pair(mid):  
      bottom = mid - 1  
    else:  
      top = mid + 1   

  return top - 1

if __name__ == '__main__':
  R, C = map(int, input().split())
  strs = [str(input().rstrip()) for _ in range(R)]

  print(find_biggest_index_with_no_same_string())