import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**8)

def get_power_of_2(n):
    if n < len(powers_of_2):
        return powers_of_2[n]

    if n % 2 == 0:
        return get_power_of_2(n // 2) ** 2 % MOD
    else:
        return (get_power_of_2(n // 2) ** 2 % MOD) * 2

MOD = 10**9+7

N = int(input())

powers_of_2 = []
cur = 1
while cur <= 100000:
    powers_of_2.append(cur)
    cur = (cur * 2) % MOD

result = 0
# ax^b -> abx^(b-1)
for _ in range(N):
    N, C = map(int, input().split())
    result = (result + ((N * C % MOD) * get_power_of_2(C - 1)) % MOD) % MOD

print(result)