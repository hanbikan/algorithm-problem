import sys
input = sys.stdin.readline

N = int(input())
x = list(map(int, input().split()))

'''
9
52853 1 3213 523489 5829 5 4199571 4817394 8
'''

result = float('inf')
for i in range(N-1):
    for j in range(i+1, N):
        count = 0
        diff = x[j] - x[i]
        dist = j - i
        if diff % dist == 0:
            each_diff = diff // dist

            expect = x[i] - each_diff
            for k in range(i-1, -1, -1):
                if x[k] != expect:
                    count += 1
                expect -= each_diff

            expect = x[i] + each_diff
            for k in range(i+1, j):
                if x[k] != expect:
                    count += 1
                expect += each_diff

            expect = x[j] + each_diff
            for k in range(j+1, N):
                if x[k] != expect:
                    count += 1
                expect += each_diff

            result = min(result, count)
print(result)