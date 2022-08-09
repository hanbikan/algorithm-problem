import sys
import heapq
input = sys.stdin.readline


def initialize_queue():
    queue = []
    for i in range(1, N+1):
        if entry_levels[i] == 0:
            queue.append(i)

    return queue


def get_ordered_problems(queue):
    ordered_problems = []

    while queue:
        cur = heapq.heappop(queue)
        ordered_problems.append(cur)

        for next in info[cur]:
            entry_levels[next] -= 1

            if entry_levels[next] == 0:
                heapq.heappush(queue, next)

    return ordered_problems


if __name__ == '__main__':
    # 입력
    N, M = map(int, input().split())

    info = [[] for _ in range(N+1)]
    entry_levels = [0]*(N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        info[a].append(b)
        entry_levels[b] += 1

    # 처리
    queue = initialize_queue()
    ordered_problems = get_ordered_problems(queue)

    # 출력
    print(*ordered_problems)
