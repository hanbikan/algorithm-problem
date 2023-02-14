import sys
input = sys.stdin.readline
MOD = 10**9 + 7

def two_pow_with_mod(n):
    if n <= 0:
        return 1
    elif n == 1:
        return 2
    
    c = two_pow_with_mod(n // 2)
    if n % 2 == 0:
        return (c * c) % MOD
    else:
        return ((c * c) % MOD * 2) % MOD

T = int(input())
for _ in range(T):
    N = int(input())
    print(two_pow_with_mod(N - 2))
