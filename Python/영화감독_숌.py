import sys
input = sys.stdin.readline
  
def f(prefix_len, postfix_len):
  global res
                        
  if prefix_len == 0: 
    prefixes = [""]
  else:
    # 100 ~ 999
    prefixes = [str(i) for i in range(10**(prefix_len-1), 10**prefix_len)] 

  if postfix_len == 0:  
    postfixes = [""]
  else:
    # 000 ~ 999    
    postfixes = []
    for i in range(10**postfix_len):
      s = str(i)
      s = "0"*(postfix_len-len(s)) + s
      postfixes.append(s)
       
  for prefix in prefixes:
    for postfix in postfixes:
      res.add(int(prefix + "666" + postfix))        

if __name__ == '__main__':
  N = int(input())

  res = set()       
  additional_len = 0

  while(len(res) < N):
    # additional_len -> pre/post split
    for prefix_len in range(additional_len+1):
      postfix_len = additional_len - prefix_len    
      f(prefix_len, postfix_len)

    additional_len += 1
                           
  print(sorted(list(res))[N-1])