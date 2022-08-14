import sys
input = sys.stdin.readline
DAYS, PAGES, PPD = 0, 1, 2

def f(left_days, pages_count, start_index):
    if left_days < 0: return 0

    res = pages_count
    for i in range(start_index, M):
        days, pages, _ = days_and_pages_and_ppd[i]
        res = max(res, f(left_days - days, pages_count + pages, i + 1))

    return res


if __name__ == '__main__':
    N, M = map(int,input().split())
    # PPD: Pages per a day
    days_and_pages_and_ppd = []

    for i in range(M):
        days, pages = map(int,input().split())
        ppd = pages / days
        days_and_pages_and_ppd.append([days, pages, ppd])

    print(f(N, 0, 0))