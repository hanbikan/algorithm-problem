from sys import stdin
from math import ceil, log

input = stdin.readline
MOD = 10**9+7


def get_segment_tree_length():
    if N & (N-1) == 0:
        return 2*N
    else:
        return pow(2, ceil(log(N, 2)) + 1)


def initialize_segment_tree(index, start, end):
    if start == end:
        seg_tree[index] = nums[start]
        return

    mid = (start + end)//2
    initialize_segment_tree(index*2, start, mid)
    initialize_segment_tree(index*2+1, mid+1, end)
    seg_tree[index] = (seg_tree[index*2] + seg_tree[index*2+1]) % MOD


def update_segment_tree(index, start, end, left, right, order, value):
    propagate_segment_tree(index, start, end)

    if right < start or end < left:
        return

    if left <= start and end <= right:
        if order == 1:
            lazy1[index] = 1
            lazy2[index] = value
        elif order == 2:
            lazy1[index] = value
            lazy2[index] = 0
        else:
            lazy1[index] = 0
            lazy2[index] = value

        propagate_segment_tree(index, start, end)

        return

    mid = (start + end)//2
    update_segment_tree(index*2, start, mid, left, right, order, value)
    update_segment_tree(index*2+1, mid+1, end, left, right, order, value)
    seg_tree[index] = (seg_tree[index*2] + seg_tree[index*2+1]) % MOD


def query_segment_tree(index, start, end, left, right):
    propagate_segment_tree(index, start, end)

    if right < start or end < left:
        return 0

    if left <= start and end <= right:
        return seg_tree[index]

    mid = (start + end)//2
    return (query_segment_tree(index*2, start, mid, left, right) + query_segment_tree(index*2+1, mid+1, end, left, right)) % MOD


def propagate_segment_tree(index, start, end):
    if not (lazy1[index] == 1 and lazy2[index] == 0):
        seg_tree[index] = seg_tree[index]*lazy1[index] + \
            (end - start + 1)*lazy2[index]

        if start != end:
            lazy1[index*2] = (lazy1[index*2]*lazy1[index]) % MOD
            lazy1[index*2+1] = (lazy1[index*2+1]*lazy1[index]) % MOD
            lazy2[index*2] = (lazy2[index*2]*lazy1[index] + lazy2[index]) % MOD
            lazy2[index*2+1] = (lazy2[index*2+1] *
                                lazy1[index] + lazy2[index]) % MOD

        lazy1[index] = 1
        lazy2[index] = 0


if __name__ == '__main__':
    N = int(input())
    nums = [-1] + list(map(int, input().split()))

    seg_length = get_segment_tree_length()
    seg_tree = [0]*seg_length
    lazy1 = [1]*seg_length
    lazy2 = [0]*seg_length
    initialize_segment_tree(1, 1, N)

    M = int(input())
    for _ in range(M):
        cur = list(map(int, input().split()))
        if cur[0] == 1 or cur[0] == 2 or cur[0] == 3:
            update_segment_tree(1, 1, N, cur[1], cur[2], cur[0], cur[3])
        else:
            print(query_segment_tree(1, 1, N, cur[1], cur[2]))
