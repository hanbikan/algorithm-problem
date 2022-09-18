from collections import deque
import sys
input = sys.stdin.readline

def query_info(info, data):
    res = 0
    for info_item in info:
        is_success = True
        for k in range(4):
            if not (data[k] == '-' or info_item[k] == data[k]):
                is_success = False
                break

        if is_success and int(info_item[-1]) >= int(data[-1]):
            res += 1
    
    return res


def solution(info, query):
    answer = deque()

    for i in range(len(info)):
        info[i] = info[i].split()

    for q in query:
        a, b, c, d = q.split('and')
        d, e = d.split()
        data = a.strip(), b.strip(), c.strip(), d.strip(), e.strip()
        cur_item_count = query_info(info, data)
        answer.append(cur_item_count)

    return list(answer)

N = int(input())
info = [str(input().rstrip()) for _ in range(N)]

M = int(input())
query = [str(input().rstrip()) for _ in range(M)]

print(solution(info, query))