import sys
input = sys.stdin.readline


def solution():
    K = int(input())

    area = getArea(K)
    if K == area:
        print(area, 0)
    else:
        print(area, getSliceCount(area, K-area//2))


def getArea(n):
    area = 1

    while area < n:
        area *= 2

    return area


def getSliceCount(area, index):
    offset = area//8
    sliceCount = 2
    todo = [area//4]

    while True:
        nextTodo = []

        for idx in todo:
            if idx == index:
                return sliceCount
            nextTodo += [idx+offset, idx-offset]

        offset //= 2
        sliceCount += 1
        todo = nextTodo


if(__name__ == '__main__'):
    solution()
