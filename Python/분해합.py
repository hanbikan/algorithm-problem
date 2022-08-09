import sys
input = sys.stdin.readline

def f(n):
  res = n
  for c in str(n):
    res += int(c)
  return res

if __name__ == '__main__':
  N = int(input())   
  for i in range(1, N):
    if f(i) == N:
      print(i)
      break
  else:
    print(0)