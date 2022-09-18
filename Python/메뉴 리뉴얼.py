from collections import defaultdict
from itertools import combinations
import sys
input = sys.stdin.readline

def solution(orders, course):
    answer = []

    dictt = defaultdict(int)
    for order in orders:
        for n in course:
            for cb in combinations(order, n):
                lcb = list(cb)
                lcb.sort()
                strr = ''.join(lcb)
                dictt[strr] += 1
    
    max_count_by_length = {i: 0 for i in course}
    for strr, count in dictt.items():
        if count >= 2:
            max_count_by_length[len(strr)] = max(max_count_by_length[len(strr)], count)
    
    for strr, count in dictt.items():
        if max_count_by_length.get(len(strr)) and max_count_by_length[len(strr)] == count:
            answer.append(strr)

    answer.sort()
    return answer

orders = list(map(str, input().rstrip().split()))
course = list(map(int, input().split()))

print(solution(orders, course))