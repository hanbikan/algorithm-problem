import heapq
import sys
from collections import deque

input = sys.stdin.readline


def solution():
    dq = deque(priorities)
    pq = [-p for p in priorities]  # max heap
    heapq.heapify(pq)

    target_index = M
    printed = 0
    while dq:
        max_value = -heapq.heappop(pq)
        if max_value == dq[0]:  # 가장 앞에 있는 문서의 중요도가 가장 큰가?
            # 맨 앞 문서(pq에서 가장 큰 값) 제거
            dq.popleft()
            printed += 1
            if target_index == 0:  # 인쇄 순서가 궁금한 문서인가?
                return printed
        else:
            # 맨 앞 문서를 맨 뒤로 보냄
            removed = dq.popleft()
            dq.append(removed)
            # pq 복구
            heapq.heappush(pq, -max_value)

        target_index = (target_index + len(dq) - 1) % len(dq)


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    result = solution()
    print(result)
