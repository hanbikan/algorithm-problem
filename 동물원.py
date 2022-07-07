import sys
input = sys.stdin.readline
MOD = 9901

if __name__ == '__main__':
    N = int(input())

    pair = [1, 3]
    index_to_modify = 0

    for _ in range(2, N+1):
        pair[index_to_modify] = (pair[index_to_modify] + pair[(index_to_modify+1)%2]*2) % MOD
        index_to_modify = (index_to_modify + 1) % 2

    print(pair[(index_to_modify + 1)%2])