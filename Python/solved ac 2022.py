import sys
input = sys.stdin.readline

days_count = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

def calculate_accurate_hour(time):
    y, mon, d, h, min, s = time
    result = s / (60 * 60)
    result += min / 60
    result += h
    result += (d - 1) * 24
    for cur_m in range(1, mon):
        result += days_count[cur_m] * 24
        if y == 2020 and cur_m == 2: result += 24
    result += (y - 1) * 365 * 24
    if y > 2020: result += 24
    return result

def calculate_p(i):
    h1, h2 = calculate_accurate_hour(times[-1]), calculate_accurate_hour(times[i])
    year_diff = (h1 - h2) / (24 * 365)
    return max(0.5**year_diff, 0.9**(N - (i + 1)))

def calculate_difficulty():
    if N == 0:
        return 0
    elif N == 1:
        return difficulties[0]

    p = []
    for i in range(N):
        p.append(calculate_p(i))

    numerator = 0
    denominator = 0
    for i in range(N):
        numerator += p[i] * difficulties[i]
        denominator += p[i]

    return round(numerator / denominator)

N = int(input())
times = []
difficulties = []
for _ in range(N):
    ymd, hms, difficulty = input().split()
    year, month, day = int(ymd[:4]), int(ymd[5:7]), int(ymd[8:])
    hour, minute, second = int(hms[:2]), int(hms[3:5]), int(hms[6:])

    times.append((year, month, day, hour, minute, second))
    difficulties.append(int(difficulty))

print(calculate_difficulty())