import sys
input = sys.stdin.readline

def solution(cap, n, deliveries, pickups):
    res = 0

    tmp1 = []
    cd = cap
    i = n-1
    while i >= 0:
        d = deliveries[i]

        if d > 0:
            if cd == cap:
                tmp1.append(i+1)

            diff = min(d, cd)
            cd -= diff
            deliveries[i] -= diff

            if cd == 0:
                cd = cap

        if deliveries[i] == 0:
            i -= 1

    tmp2 = []
    cp = cap
    i = n-1
    while i >= 0:
        p = pickups[i]

        if p > 0:
            if cp == cap:
                tmp2.append(i+1)

            diff = min(p, cp)
            cp -= diff
            pickups[i] -= diff

            if cp == 0:
                cp = cap

        if pickups[i] == 0:
            i -= 1
        
    for i in range(max(len(tmp1), len(tmp2))):
        t1 = tmp1[i] if i <= len(tmp1) - 1 else 0
        t2 = tmp2[i] if i <= len(tmp2) - 1 else 0
        res += max(t1, t2)*2

    return res


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
