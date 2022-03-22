import sys
input = sys.stdin.readline

if __name__ == '__main__':
  M = int(input())     
  a = []
  a_sum = 0
  a_xor = 0

  for _ in range(M):
    param = list(map(int, input().split()))

    if param[0] == 1:
      a.append(param[1])
      a_sum += param[1]
      a_xor ^= param[1]
    elif param[0] == 2:
      a_sum -= param[1]
      a_xor ^= param[1]   
    elif param[0] == 3:
      print(a_sum)
    else:     
      print(a_xor)