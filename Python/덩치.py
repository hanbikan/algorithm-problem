import sys
input = sys.stdin.readline
                    
if __name__ == '__main__':
  N = int(input())
  info = [list(map(int, input().split())) for _ in range(N)]   

  for i in range(N):
    count = 1
    x, y = info[i]

    for j in range(N):
      nx, ny = info[j]

      if x < nx and y < ny:
        count += 1

    print(count, end=" ")