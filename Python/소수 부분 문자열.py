from math import sqrt
import sys
input = sys.stdin.readline

def check_is_prime(number):
    for i in range(2, int(sqrt(number))+1):
        if number % i == 0:
            return False
    return True

is_prime = [True]*100001
is_prime[1] = False
for i in range(2, 100001):
    if is_prime[i]:
        if check_is_prime(i):
            j = 2
            while i*j < 100001:
                is_prime[i*j] = False
                j += 1

primes = []
for i in range(2, 100001):
    if is_prime[i]:
        primes.append(i)

while True:
    n = input().rstrip()
    if n == "0": break

    maxx = 0
    for s in range(len(n)-1):
        for e in range(s+1, len(n)):
            n_as_int = int(n[s:e])
            if n_as_int <= 100000 and is_prime[n_as_int]:
                maxx = max(maxx, n_as_int)
    print(maxx)