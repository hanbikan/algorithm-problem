import sys
input = sys.stdin.readline


class Node():
    def __init__(self, key, is_ended=False):
        self.key = key
        self.is_ended = is_ended
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, strings):
        current_node = self.head

        for string in strings:
            # 없다면 생성
            if string not in current_node.children:
                current_node.children[string] = Node(string)

            current_node = current_node.children[string]

        # 플래그 수정
        current_node.is_ended = True

    def dfs(self, current_node, depth):
        for k, v in sorted(current_node.children.items()):
            # 출력
            for _ in range(depth):
                print("--", end="")
            print(k)

            # 재귀
            self.dfs(v, depth + 1)


if __name__ == '__main__':
    N = int(input())

    trie = Trie()
    for _ in range(N):
        cur_input = list(map(str, input().split()))
        trie.insert(cur_input[1:])

    trie.dfs(trie.head, 0)
