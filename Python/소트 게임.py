import sys
input = sys.stdin.readline

def f():
    visited = set()
    visited.add(tuple(nums))

    q = [nums]
    count = 0

    while(len(q) > 0):
        nq = []

        while(len(q) > 0):
            cur = q.pop(0)
            if cur == sorted_nums:
                return count

            for i in range(N-K+1):
                to_append = cur[:i] + cur[i:i+K][::-1] + cur[i+K:]

                if not tuple(to_append) in visited:
                    nq.append(to_append)
                    visited.add(tuple(to_append))
                
        q = nq
        count += 1
    
    return -1

if __name__ == '__main__':
    N, K = map(int,input().split())
    nums = list(map(int,input().split()))
    sorted_nums = sorted(nums)
    print(f())