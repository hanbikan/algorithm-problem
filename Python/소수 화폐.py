import sys
input = sys.stdin.readline

MOD = 123_456_789
N = int(input())

# Get prime numbers
primes = []
is_prime = [False, False] + [True] * (N - 1)
for i in range(2, N + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(2*i, N + 1, i):
            is_prime[j] = False

dp = [0] * (N + 1)
dp[0] = 1 # dp[5] = dp[5] + dp[0]
for p in primes: # max: 4203
    for i in range(p, N + 1):
        dp[i] = (dp[i] + dp[i - p]) % MOD
print(dp[-1])