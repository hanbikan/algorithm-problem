import sys
input = sys.stdin.readline

def int_list_to_int(lst):
    return int("".join(str(x) for x in lst))

# 123 -> 100
def get_10_base(num):
    i = 1
    while i * 10 <= num:
        i *= 10
    return i

def f(n):
    if n < 10:
        for i in range(1, n + 1):
            result[i] += 1
        return

    first_digit = int(str(n)[0])
    base_10 = get_10_base(n)

    all_nine = True
    for i in range(len(str(n))):
        c = str(n)[i]
        if c != '9':
            all_nine = False
            break

    # 999
    if all_nine:
        cur_nines = nines[len(str(n)) - 1]
        for i in range(len(cur_nines)):
            result[i] += cur_nines[i]
        return


    # >= 10
    # 385 -> 300 + f(99) for 286 ~ 385 + f(285)
    a = base_10 - 1
    b = n - base_10
    f(a)
    f(b)

    # 300
    for c in str(first_digit * base_10):
        result[ord(c) - ord('0')] += 1

    # count 0
    cur = 10
    while cur < base_10:
        result[0] += min(cur - 1, b)
        cur *= 10

    # 301~385 + 286~299
    ld = int(str(n)[1:]) # 1~85 -> 85
    result[first_digit] += ld
    if first_digit - 1 >= 1:
        result[first_digit - 1] += base_10 - ld - 1 # 86~99 -> 14

N = int(input())

nines = [
    [0,1,1,1,1,1,1,1,1,1],
    [9,20,20,20,20,20,20,20,20,20],
]
i = 2
cur = 999
while cur <= 1_000_000_000:
    a = [i - 1] + [8]*(i - 1) + [9]
    nines.append(
        [int_list_to_int(a)] + [(i + 1) * ((cur + 1) // 10)] * 9
    )

    cur = cur * 10 + 9
    i += 1

result = [0]*10
f(N)
print(*result)