import sys
input = sys.stdin.readline

def f(index, order, selected_indexes):
    if index == N:
        return calculate(order)

    res = 0
    for i in range(N):
        if i in selected_indexes:
            continue
        selected_indexes.add(i)
        res = max(res, f(index + 1, order + [nums[i]], selected_indexes))
        selected_indexes.remove(i)

    return res

def calculate(order):
    return sum(abs(order[i] - order[i+1]) for i in range(N-1))

N = int(input())
nums = list(map(int,input().split()))

print(f(0, [], set()))