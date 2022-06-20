from logging import root
import sys
input = sys.stdin.readline

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, strr):
        cur = self.root
        for c in strr:
            index = ord(c) - ord('a')
            if cur.childs[index] == None:
                cur.childs[index] = Node()
            cur = cur.childs[index]

    def find(self, strr):
        cur = self.root
        for c in strr:
            index = ord(c) - ord('a')
            if cur.childs[index] == None:
                return False
            cur = cur.childs[index]
        return True

class Node:
    def __init__(self):
        self.childs = [None]*26

if __name__ == '__main__':
    N, M = map(int, input().split())
    S1 = [str(input().rstrip()) for _ in range(N)]
    S2 = [str(input().rstrip()) for _ in range(M)]

    trie = Trie()
    for strr in S1:
        trie.insert(strr)
    
    count = 0
    for strr in S2:
        if trie.find(strr):
            count += 1

    print(count)