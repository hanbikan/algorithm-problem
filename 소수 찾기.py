import sys
input = sys.stdin.readline


def isPrimeNumber(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    primeCnt = 0
    end = max(nums)
    isPrimeNumberList = [True]*(end+1)
    isPrimeNumberList[1] = False

    for i in range(2, end+1):
        if isPrimeNumberList:
            if isPrimeNumber(i):
                cur = i*2
                j = 2
                while cur <= end:
                    isPrimeNumberList[cur] = False
                    j += 1
                    cur = i*j

    for num in nums:
        if isPrimeNumberList[num]:
            primeCnt += 1

    print(primeCnt)


N = int(input())
nums = list(map(int, input().split()))

solution(nums)
