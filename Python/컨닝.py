import sys
input = sys.stdin.readline

def get_formatted_bit(bit):
    return bin(bit)[2:][::-1]

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    mapp = []
    for _ in range(N):
        line = list(input().rstrip())
        mapp.append(line)

    bits_for_x = [0]
    for j in range(M):
        bit_for_x = 0
        for i in range(N):
            if mapp[i][j] == 'x':
                bit_for_x |= 1 << i
        bits_for_x.append(bit_for_x)

    result = 0
    dp = [[0]*(2**N) for _ in range(M + 1)]
    for j in range(M):
        if j - 1 >= 0:
            dp[j + 1][0] = result
        for i in range(N):
            if mapp[i][j] == 'x':
                continue

            for cur_bit in range(1 << i):
                if cur_bit & bits_for_x[j + 1] != 0:
                    continue
                cur_bit_masked = cur_bit | (1 << i)

                cur_bit_1_count = 0
                test_bit = 0
                tmp_index = 0
                tmp_cur_bit = cur_bit_masked
                while tmp_cur_bit > 0:
                    if tmp_cur_bit & 1 == 1:
                        cur_bit_1_count += 1

                        for k in range(tmp_index - 1, tmp_index + 2):
                            if 0 <= k <= N - 1:
                                test_bit = test_bit | (1 << k)

                    tmp_index += 1
                    tmp_cur_bit //= 2

                for prev_bit in range(1 << N):
                    if prev_bit & test_bit == 0:
                        dp[j + 1][cur_bit_masked] = max(
                            dp[j + 1][cur_bit_masked],
                            dp[j][prev_bit] + cur_bit_1_count,
                        )
                        result = max(result, dp[j + 1][cur_bit_masked])

    print(result)