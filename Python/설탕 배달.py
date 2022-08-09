def solution(N):
    LargestPossibleAmountof5 = N//5
    for i in range(LargestPossibleAmountof5, -1, -1):
        Remainder = N-i*5
        if Remainder%3 == 0:
            return i + Remainder//3
    return -1

N = int(input())
print(solution(N))