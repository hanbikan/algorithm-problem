import sys
input = sys.stdin.readline


def initializeMins(index, start, end):
    if start == end:
        mins[index] = input_nums[start]
        return mins[index]

    mid = (start+end)//2
    left_min = initializeMins(index*2, start, mid)
    right_min = initializeMins(index*2+1, mid+1, end)

    mins[index] = min(left_min, right_min)

    return mins[index]


def queryMins(index, range, start, end):
    if end < range[0] or range[1] < start:
        return float('inf')

    if range[0] <= start and end <= range[1]:
        return mins[index]

    mid = (start+end)//2
    left_min = queryMins(index*2, range, start, mid)
    right_min = queryMins(index*2+1, range, mid+1, end)

    return min(left_min, right_min)


if __name__ == '__main__':
    while True:
        input_nums = list(map(int, input().split()))
        if input_nums == [0]:
            break
        input_len = len(input_nums)

        mins = [0]*(4*input_len)
        initializeMins(1, 0, input_len-1)

        max_sum = 0
        for i in range(input_len):
            for j in range(i, input_len):
                max_sum = max(max_sum, queryMins(
                    1, (i, j), 0, input_len-1)*(j-i+1))
        print(max_sum)
