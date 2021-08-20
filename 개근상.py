import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())

    o, a, aa, lo, la, laa = 1, 1, 0, 1, 0, 0
    for i in range(N-1):
        o, a, aa, lo, la, laa = o + a + aa, o, a, o + a + aa + lo + la + laa, lo, la

    print((o + a + aa + lo + la + laa) % 1000000)
