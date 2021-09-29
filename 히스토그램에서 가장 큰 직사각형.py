import sys
input = sys.stdin.readline


def solution(nums):
    res = 0

    length = nums[0]
    stack = [0]  # 인덱스를 저장
    nums[0] = 0  # 반복문 초기에 nums[stack[0]], 즉 nums[0]과 값을 비교하는데, 이에 대한 처리임
    nums.append(0)  # 마지막 인덱스에서의 연산을 위함

    for i in range(1, length+2):
        while nums[stack[-1]] > nums[i]:
            index = stack.pop()
            res = max(res, (i - (stack[-1] + 1))*nums[index])

        stack.append(i)

    return res


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    while nums[0] != 0:
        print(solution(nums))
        nums = list(map(int, input().split()))
