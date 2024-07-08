import bisect
import sys
input = sys.stdin.readline

'''
<고리 n개를 풀 때의 최적화 방식>
n=1 -> 2 1 4
n=2 -> 3 1 6 1 12
    해설: 앞에 (3 1)을 두는 이유는 뒤에 1을 하나 더 쓸 수 있으므로 이것만으로 5까지 만들 수 있기 때문임. 뒤에 6이 붙는 건 6은 만들 수 없기 때문
n=3 -> 4 1 8 1 16 1
n=n -> (n+1)*2^0 1 (n+1)*2^1 1 (n+1)*2^2 1 ... (n+1)*2^n = (n+1)*(2^(n+1) - 1) + n = (2^(n+1))(n+1) - 1
'''

def f(x):
    return (pow(2, x + 1)) * (x + 1) - 1

MAX = 10**18
N = int(input())

ends = [1]
i = 1
while True:
    cur = f(i)
    if cur > MAX:
        break
    ends.append(cur)
    i += 1
index = bisect.bisect_left(ends, N)
print(index)