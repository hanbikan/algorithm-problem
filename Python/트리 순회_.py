import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def f(node: Node, h):
    if node == None: return

    global last_height
    f(node.left, h+1)
    last_height = h
    f(node.right, h+1)

N = int(input())
nodes = [None] + [Node(i, None, None) for i in range(1, N+1)]
for _ in range(N):
    a, b, c = map(int, input().split())
    if b != -1: nodes[a].left = nodes[b]
    if c != -1: nodes[a].right = nodes[c]

last_height = 0
f(nodes[1], 0)
print((N-1)*2 - last_height)