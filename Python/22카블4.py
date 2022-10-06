import sys
input = sys.stdin.readline

class Node:
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None

def make_tree(height):
    root = Node(-1)
    roots = [root]
    for i in range(height-1):
        next_roots = []
        for r in roots:
            r.left = Node(-1)
            r.right = Node(-1)
            next_roots.append(r.left)
            next_roots.append(r.right)
        roots = next_roots
    return root

def construct_tree(node: Node):
    if node == None: return

    construct_tree(node.left)
    global index
    node.num = int(binn[index])
    index += 1
    construct_tree(node.right)

def check_tree(node: Node):
    if node == None: return True

    if node.num == 0:
        if (node.left != None and node.left.num == 1) or (node.right != None and node.right.num == 1):
            return False
    
    return check_tree(node.left) and check_tree(node.right)

def f(n):
    global binn, index
    binn = list(bin(n))[2:]
    
    height = 1
    i = 1
    while True:
        i *= 2
        if i > len(binn): break
        height += 1
    binn = ['0']*(2**height - len(binn) - 1) + binn
    root = make_tree(height)
    index = 0
    construct_tree(root)
    
    return 1 if check_tree(root) else 0

def solution(numbers):
    answer = []
    for n in numbers:
        answer.append(f(n))
    return answer

print(solution([7,5,63,111,95]))