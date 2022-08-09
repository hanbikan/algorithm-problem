import sys
input = sys.stdin.readline
dx = [0, 1, 0, -1, 0]
dy = [0, 0, 1, 0, -1]
INF = 101


def is_turned_on(status, x, y):
    return status[x] & (1 << (9 - y)) != 0


def do_click(status, x, y):
    y = 9 - y
    for i in range(5):
        cur_x, cur_y = x + dx[i], y + dy[i]
        if 0 <= cur_x <= 9 and 0 <= cur_y <= 9:
            status[cur_x] = status[cur_x] ^ (1 << cur_y)

    return status


def is_done(status):
    return sum(status) == 0


def solution(status):
    res = INF

    for l in range(1 << 10):
        cnt = 0

        # 새 리스트 생성
        new_status = []
        for i in range(10):
            new_status.append(status[i])

        # l에 따른 클릭
        for i in range(10):
            if l & (1 << (9 - i)) != 0:
                new_status = do_click(new_status, 0, i)
                cnt += 1

        # 현 상태부터 카운트 시작
        for i in range(1, 10):
            for j in range(10):
                # 조건: 바로 위에 있는 것이 켜져있을 경우
                if is_turned_on(new_status, i-1, j):
                    new_status = do_click(new_status, i, j)
                    cnt += 1

        # 불이 다 꺼졌을 경우에만 res 값 갱신
        if is_done(new_status):
            res = min(res, cnt)

    return res if res != INF else -1


if __name__ == '__main__':
    status = []
    for _ in range(10):
        to_append = 0
        cur_input = str(input().rstrip())
        for i in range(9, -1, -1):
            if cur_input[9-i] == 'O':
                to_append = to_append | 1 << i
        status.append(to_append)

    print(solution(status))
