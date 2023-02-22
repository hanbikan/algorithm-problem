import sys
input = sys.stdin.readline

def calculate_point(w, l):
    res = 2000
    for _ in range(w): res += 50
    for _ in range(l): res -= 50
    return res

def f(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

# nCr
def c(n, r):
    if n == r or r == 0:
        return 1
    return f(n) // (f(r) * f(n - r))

W, L, D = map(float, input().split())

bronze = 0.0
silver = 0.0
gold = 0.0
platinum = 0.0
diamond = 0.0

for w in range(21):
    for l in range(21 - w):
        d = 20 - (w + l)

        posibility = (pow(W, w) * pow(L, l) * pow(D, d)) * (c(20, w) * c(20 - w, l))
        point = calculate_point(w, l)

        if point >= 3000:
            diamond += posibility
        elif point >= 2500:
            platinum += posibility
        elif point >= 2000:
            gold += posibility
        elif point >= 1500:
            silver += posibility
        else:
            bronze += posibility

print('{0:.8f}'.format(bronze))
print('{0:.8f}'.format(silver))
print('{0:.8f}'.format(gold))
print('{0:.8f}'.format(platinum))
print('{0:.8f}'.format(diamond))