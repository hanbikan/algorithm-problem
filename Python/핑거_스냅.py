import sys, math
input = sys.stdin.readline

def check_is_prime(n):
  for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
      return False
  return True

def set_is_prime():
  global is_prime
  is_prime[1] = False
  for i in range(2, 100001):
    if is_prime[i]:
      if check_is_prime(i):
        for j in range(i*2, 100001, i):
          is_prime[j] = False
                   
def f(n):
  is_visited = [False]*1000001
  is_visited[n] = True
  q = [n]
  count = 0

  while(len(q) != 0):
    nq = []

    while(len(q) != 0):
      cur = q.pop(0)

      if A <= cur <= B and is_prime[cur]:
        return count

      nxt = cur//2
      if 0 <= nxt <= 1000000 and not is_visited[nxt]:
        is_visited[nxt] = True
        nq.append(nxt)
             
      nxt = cur//3
      if 0 <= nxt <= 1000000 and not is_visited[nxt]:
        is_visited[nxt] = True
        nq.append(nxt)

      nxt = cur+1
      if 0 <= nxt <= 1000000 and not is_visited[nxt]:
        is_visited[nxt] = True
        nq.append(nxt)

      nxt = cur-1
      if 0 <= nxt <= 1000000 and not is_visited[nxt]:
        is_visited[nxt] = True
        nq.append(nxt)       

    count += 1
    q = nq

  return -1

   
if __name__ == '__main__':
  is_prime = [True]*100001
  set_is_prime()                

  for _ in range(int(input())):
    N, A, B = map(int, input().split())     
    print(f(N))