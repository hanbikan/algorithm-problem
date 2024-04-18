import sys

input = sys.stdin.readline

S = str(input().rstrip())
P = str(input().rstrip())

copy_count = 0
pi = 0
while pi < len(P):
    # find max overlap length
    max_overlap_length = 0
    for start_si in range(len(S)):
        cur_pi = pi
        while S[start_si] == P[cur_pi]:
            start_si += 1
            cur_pi += 1
            if start_si >= len(S) or cur_pi >= len(P):
                break
        cur_length = cur_pi - pi
        max_overlap_length = max(max_overlap_length, cur_length)

    pi += max_overlap_length
    copy_count += 1

print(copy_count)