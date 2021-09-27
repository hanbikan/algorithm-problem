import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def get_tree_length(N):
    if N & (N-1) == 0:
        return 2*N
    else:
        return pow(2, math.ceil(math.log(N, 2)) + 1)


def initialize_segtree(index, start, end):
    if start == end:
        tree[index] = start
        return

    mid = (start + end)//2
    initialize_segtree(index*2, start, mid)
    initialize_segtree(index*2+1, mid+1, end)

    # Returns lower one
    if nums[tree[index*2]] < nums[tree[index*2+1]]:
        tree[index] = tree[index*2]
    else:
        tree[index] = tree[index*2+1]


def query_segtree(index, start, end, left, right):
    # For an exception
    if right < start or end < left:
        return -1

    if left <= start and end <= right:
        return tree[index]

    mid = (start+end)//2
    l = query_segtree(index*2, start, mid, left, right)
    r = query_segtree(index*2+1, mid+1, end, left, right)

    # Handle out of range exception
    if l == -1 or r == -1:
        return max(l, r)
    else:
        # Returns lower one
        if nums[l] < nums[r]:
            return l
        else:
            return r


def get_square_area(start, end):
    if start == end:
        return nums[start]

    # Get lowest height
    index = query_segtree(1, 1, nums[0], start, end)
    areas = [(end-start+1)*nums[index]]

    # Is in range?
    if index-1 >= start:
        areas.append(get_square_area(start, index-1))
    if index+1 <= end:
        areas.append(get_square_area(index+1, end))

    return max(areas)


if __name__ == '__main__':
    # Do while
    nums = list(map(int, input().split()))
    while nums[0] != 0:
        # Initialize segment tree
        tree = [0]*get_tree_length(nums[0])
        initialize_segtree(1, 1, nums[0])

        # Solution
        print(get_square_area(1, nums[0]))

        # Get next input
        nums = list(map(int, input().split()))
