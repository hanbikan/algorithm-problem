import sys
input = sys.stdin.readline


def getMaxScore(nums, N):
    if N == 1:
        return nums[0]

    score = 0

    # 음수
    for i in range(0, N-1, 2):
        cur, next = nums[i], nums[i+1]

        if cur < 0 and next < 0:
            score += cur * next
        else:
            if cur < 0 and next > 0:
                score += cur
            break

    # 전부 음수이면서 N이 3이상 홀수일 때의 반례
    if i+2 == N-1:
        if nums[N-1] < 0:
            score += nums[N-1]

    # 양수
    addPoint = 0
    for i in range(N-1, 0, -2):
        cur, next = nums[i], nums[i-1]

        if cur > 1 and next > 1:
            score += cur * next
        else:
            addPoint = i
            break

    # 나머지 양수들 더하기
    for i in range(addPoint, -1, -1):
        if nums[i] >= 1:
            score += nums[i]
        else:
            break

    return score


if __name__ == '__main__':
    N = int(input())
    nums = [int(input()) for _ in range(N)]

    nums.sort()

    maxScore = getMaxScore(nums, N)
    print(maxScore)
