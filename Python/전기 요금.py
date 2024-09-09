import sys
input=sys.stdin.readline

# 요금 그래프: 기울기가 증가하는 일차함수 여러 개
# 1~100: y = 2x ... y: 0~200
# 101~10000: 3 -> y = 3(x-100) + 200 = 3x - 100 ... y: 200~29900
# 10001~1000000: 5(x-10000) + 29900 = 5x - 20100 ... y: 29900~4979900
# 1000001~ : 7(x-1000000) + 4979900 = 7x - 2020100 ... y: 4979900~
# reversed


def calc_w_by_price(p):
    if 0 <= p <= 200:
        return p / 2
    elif 200 < p <= 29900:
        return (p - 200)/3 + 100
    elif 29900 < p <= 4979900:
        return (p - 29900)/5 + 10000
    else:
        return (p - 4979900)/7 + 1000000

while True:
    A, B = map(int, input().split()) # 1100: 요금 합, 300: 요금 차이
    if A == B == 0:
        break

    l, r = 0, A

    while l <= r:
        m = (l + r) // 2
        pa = m
        wa = calc_w_by_price(pa)

        pb = pa + B
        wb = calc_w_by_price(pb)

        wab = wa + wb
        if 0 <= wab <= 100:
            pab = 2 * wab
        elif 100 < wab <= 10000:
            pab = 3 * wab - 100
        elif 10000 < wab <= 1000000:
            pab = 5 * wab - 20100
        else:
            pab = 7 * wab - 2020100

        if pab == A:
            print(pa)
            break
        elif pab < A:
            l = m + 1
        else:
            r = m - 1