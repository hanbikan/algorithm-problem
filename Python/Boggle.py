import sys
input = sys.stdin.readline
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

POINTS = [0, 0, 0, 1, 1, 2, 3, 5, 11]
LENGTH = 4


class Node:
    def __init__(self):
        self.children = {}
        self.is_ended = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current_node = self.root

        for c in word:
            if not current_node.children.get(c):
                current_node.children[c] = Node()

            current_node = current_node.children[c]

        current_node.is_ended = True

    def search(self, current_node, x, y, current_word):
        is_visited[x][y] = True

        # 단어가 처음 발견되었을 때
        if current_node.is_ended and (not current_word in found_nodes):
            global point, largest_word, word_count

            # 가장 긴 단어 갱신
            if len(largest_word) < len(current_word):
                largest_word = current_word
            elif len(largest_word) == len(current_word):
                # 사전순
                if largest_word > current_word:
                    largest_word = current_word

            point += POINTS[len(current_word)]
            word_count += 1

            found_nodes.add(current_word)

        # 탐색
        for i in range(8):
            nextX, nextY = x + dx[i], y + dy[i]
            if (0 <= nextX <= LENGTH-1 and 0 <= nextY <= LENGTH-1) and is_visited[nextX][nextY] == False:
                n = grid[nextX][nextY]
                if current_node.children.get(n):
                    self.search(
                        current_node.children[n], nextX, nextY, current_word+n)

        is_visited[x][y] = False


if __name__ == '__main__':
    trie = Trie()
    is_visited = [[False]*LENGTH for _ in range(LENGTH)]

    w = int(input())
    for _ in range(w):
        trie.insert(str(input().rstrip()))
    _ = input()

    b = int(input())
    for i in range(b):
        grid = [str(input().rstrip()) for _ in range(LENGTH)]
        if i != b-1:
            _ = input()

        # 초기화
        found_nodes = set()
        point = 0
        largest_word = ""
        word_count = 0

        # 현재 grid에 대해 탐색
        for x in range(LENGTH):
            for y in range(LENGTH):
                c = grid[x][y]
                if trie.root.children.get(c):
                    trie.search(trie.root.children[c], x, y, c)

        # 출력
        print(point, largest_word, word_count)
