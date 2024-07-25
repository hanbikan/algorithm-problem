import sys

input = sys.stdin.readline

LEN = ord('z') - ord('a') + 1


class Node:
    def __init__(self, value):
        self.value = value
        self.nexts = {}
        self.count = 0
        self.cur_chars = []
        self.is_end = False

def char_list_to_str(char_list):
    return ''.join(char_list)

def add_word(prev_node: Node, word, index):
    prev_node.count += 1
    if index >= len(word):
        prev_node.is_end = True
        return

    c = word[index]
    if not prev_node.nexts.get(c):
        prev_node.nexts[c] = Node(c)

    prev_node.nexts[c].cur_chars = prev_node.cur_chars + [word[index]]
    add_word(prev_node.nexts[c], word, index + 1)

def set_max_depth(node, depth):
    global max_depth, max_prefix
    if node.count >= 2 and depth > max_depth:
        max_depth = depth
        max_prefix = node.cur_chars

    for c, next_node in node.nexts.items():
        set_max_depth(next_node, depth + 1)

def set_max_words(node):
    if node.is_end and char_list_to_str(max_prefix) == char_list_to_str(node.cur_chars[:len(max_prefix)]):
        word = char_list_to_str(node.cur_chars)
        max_words.append([word_to_index[word], word])

    for c, next_node in node.nexts.items():
        set_max_words(next_node)

def dfs(node, depth):
    if depth >= max_depth and node.count >= 2:
        set_max_words(node)
    else:
        for c, next_node in node.nexts.items():
            dfs(next_node, depth + 1)

N = int(input())
words = [input().rstrip() for _ in range(N)]

root = Node(None)
word_to_index = {}
for i in range(N):
    word = words[i]
    add_word(root, word, 0)
    word_to_index[word] = i

max_depth = 0
max_prefix = []
set_max_depth(root, 0)

max_words = []
dfs(root, 0)
max_words.sort()

print(max_words[0][1])
print(max_words[1][1])

'''
6
abcd
abe
abc
abchldp
qwer
qwe
'''