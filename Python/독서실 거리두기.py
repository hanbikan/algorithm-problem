import sys
input = sys.stdin.readline

# 시간 표현: 1005 -> 60 + 5 = 75
def convert_to_int(hour, minute):
    return (hour - 9) * 60 + minute

def find_seat(seats):
    if len(seats) == 0:
        return 0

    sorted_seats = sorted(seats)
    max_dist, max_seat = sorted_seats[0], 0
    for i in range(1, len(sorted_seats)):
        cur_seat = (sorted_seats[i - 1] + sorted_seats[i]) // 2
        cur_dist = min(cur_seat - sorted_seats[i - 1], sorted_seats[i] - cur_seat)
        if cur_dist > max_dist:
            max_dist = cur_dist
            max_seat = cur_seat

    end_dist = N - 1 - sorted_seats[-1]
    if end_dist > max_dist:
        max_dist = end_dist
        max_seat = N - 1

    return max_seat

def print_seats():
    for hour in range(9, 21):
        print("HOUR :", hour)
        for minute in range(0, 60):
            print(minute, ":", seats_by_int[convert_to_int(hour, minute)])

N, T, P = map(int, input().split())

seats_by_int = [set() for _ in range(convert_to_int(21, 0) + 1)]
ints = []
for _ in range(T):
    start, end = map(str, input().split())
    start_hour, start_minute = int(start[:2]), int(start[2:])
    end_hour, end_minute = int(end[:2]), int(end[2:])
    s, e = convert_to_int(start_hour, start_minute), convert_to_int(end_hour, end_minute)
    ints.append((s, e))

ints.sort(key = lambda x: x[1])
ints.sort(key = lambda x: x[0])
for s, e in ints:
    start_seats = seats_by_int[s]
    seat = find_seat(start_seats)

    for n in range(s, e):
        seats_by_int[n].add(seat)

result = 0
for seats in seats_by_int:
    if P - 1 not in seats:
        result += 1
result -= 1
print(result)

'''
2 2 1
0900 2100
0900 0910

3 4 1
0900 0915
0910 0920
0914 0930
0915 0930

6 5 1
0900 0915
0901 0915
0902 0915
0903 0915
0904 0915
'''