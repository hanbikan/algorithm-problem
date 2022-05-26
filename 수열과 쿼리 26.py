import sys
input = sys.stdin.readline
MIN, MAX = 0, 1

class SegmentTree:
    def __init__(self, size):
        self.v = [None]*size

    def init(self, index, start, end):
        if(start == end):
            self.v[index] = [A[start], A[end]]
            return

        mid = (start + end)//2
        self.init(index*2, start, mid)
        self.init(index*2+1, mid+1, end)

        self.v[index] = [
            min(self.v[index*2][MIN], self.v[index*2+1][MIN]),
            max(self.v[index*2][MAX], self.v[index*2+1][MAX])
            ]

    def update(self, index, left, right, x, start, end):
        mid = (left+right)//2
        self.update(index*2, left, mid, x, start, end)
        self.update(index*2+1, mid+1, right, x, start, end)

        self.v[index] = [
            min(self.v[index*2][MIN], self.v[index*2+1][MIN]),
            max(self.v[index*2][MAX], self.v[index*2+1][MAX])
            ]

if __name__ == '__main__':
    N = int(input())
    A = [None] + list(map(int, input().split()))
    s = SegmentTree(4*N)
    s.init(1, 1, N)
    print(s.v)

    for _ in range(int(input())):
        order = list(map(int, input().split()))
        if(order == 1):
            print()
        elif(order == 2):
            print()
        else:
            print()