import sys, itertools, random
input = sys.stdin.readline

def solution(N, M, T, K, points):
    check_points = set(points.copy())
    for cb in itertools.combinations(points, 2):
        a, b = cb
        new_point = (min(a[0], b[0]), min(a[1], b[1]))
        check_points.add(new_point)

    max_count = 0
    max_pos = (-1, -1)
    for start_x, start_y in check_points:
        end_x, end_y = start_x + K, start_y + K

        if end_x > N:
            diff = end_x - N
            start_x -= diff
            end_x -= diff

        if end_y > M:
            diff = end_y - M
            start_y -= diff
            end_y -= diff

        cur_count = 0
        for x, y in points:
            if start_x <= x <= end_x and start_y <= y <= end_y:
                cur_count += 1

        if cur_count > max_count:
            max_count = cur_count
            max_pos = (start_x, end_y)

    return max_count, max_pos

def test(N, M, T, K, points):
    max_count = 0
    max_pos = (-1, -1)

    for start_x in range(N - K + 1):
        for start_y in range(M - K + 1):
            cur_count = 0
            end_x, end_y = start_x + K, start_y + K
            for x, y in points:
                if start_x <= x <= end_x and start_y <= y <= end_y:
                    cur_count += 1
            if cur_count > max_count:
                max_count = cur_count
                max_pos = (start_x, end_y)

    return max_count, max_pos


#N, M, T, K = map(int, input().split())
#points = list(tuple(map(int, input().split())) for _ in range(T))

for t in range(1000):
    print("TEST", t)
    N = random.randrange(1, 100 + 1)
    M = random.randrange(1, 100 + 1)
    T = random.randrange(1, min(100, (N + 1) * (M + 1)) + 1)
    K = random.randrange(1, min(N, M) + 1)
    points = set()
    while len(points) < T:
        x, y = random.randrange(0, N + 1), random.randrange(0, M + 1)
        if (x, y) not in points:
            points.add((x, y))
    points = list(points)

    c1, p1 = solution(N, M, T, K, points)
    c2, p2 = test(N, M, T, K, points)

    if c1 != c2:
        print(N, M, T, K)
        print(*points)
        print(c1, p1)
        print(c2, p2)
        break