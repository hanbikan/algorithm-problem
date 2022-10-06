import sys
input = sys.stdin.readline

def f(index):
    summ = 0
    is_positive = nums[index] > 0
    for i in range(index, N):
        if is_positive and nums[i] <= 0:
            i -= 1
            break
        if not is_positive and nums[i] > 0:
            i -= 1
            break
        summ += nums[i]
    
    return summ, i

N, M = map(int,input().split())
nums = [int(input()) for _ in range(N)]

res1 = []
res2 = []
i = 0
while i < N:
    num = nums[i]
    
    cur_sum, j = f(i)
    j += 1
    if cur_sum > 0:
        while j < N:
            sum1, nj1 = f(j)
            nj1 += 1
            if nj1 > N-1: break
            sum2, nj2 = f(nj1)
            if sum1 + sum2 < 0: break
            nj2 += 1

            cur_sum += sum1 + sum2
            j = nj2
        if j - i >= M: res1.append(cur_sum)
        res2.append([cur_sum, i, j])
    
    i = j

if len(res1) == 0:
    if len(res2) == 0:
        print(0)
    else:
        
        for summ, start, end in res2:
            diff = M - (end - start)
            summ + 
        print(res2)
else:
    print(max(res1))