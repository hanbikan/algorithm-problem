import sys
input = sys.stdin.readline

def can_fill(i,j):
    if i == 0:
        return j != n-1
    elif i == n-1:
        return j != 0
    else: return j != i

if __name__ == '__main__':
    n, k = map(int, input().split())
    if n*n - k < n or (n==2 and k == 2):
        print("NO")
    else:
        print("YES")
        
        filled = 0
        for i in range(n):
            for j in range(n):
                if filled < k and can_fill(i, j):
                    print("#",end="")
                    filled += 1
                else:
                    print(".",end="")
            print()
