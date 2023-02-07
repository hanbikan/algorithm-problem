from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
words = [str(input().rstrip()) for _ in range(N)]

# Create bits
bits = []
for word in words:
    cur_bit = 0
    for c in word:
        a_index = ord(c) - ord('a')
        cur_bit |= 1 << a_index
    bits.append(cur_bit)

# Calculate the result
res = 0
for i in range(1, N+1):
    for cb in combinations(bits, i):
        cur_bit = 0
        for bit in cb:
            cur_bit |= bit
        
        if cur_bit == 0b11111111111111111111111111:
            res += 1
print(res)