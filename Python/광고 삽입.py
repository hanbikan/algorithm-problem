import sys
input = sys.stdin.readline

## hhmmss -> second
def convert_to_second(strr):
    return int(strr[0:2])*3600 + int(strr[3:5])*60 + int(strr[6:8])

def convert_to_hhmmss(second):
    return '{0:02d}:{1:02d}:{2:02d}'.format(second//3600, (second%3600)//60, second%60)

def solution(play_time, adv_time, logs):
    # 초단위로 치환
    play_time = convert_to_second(play_time)
    adv_time = convert_to_second(adv_time)
    for i in range(len(logs)):
        logs[i] = logs[i].split('-')
        for k in range(2):
            logs[i][k] = convert_to_second(logs[i][k])
    
    counts = [0]*(play_time+1)
    starts = [logs[i][0] for i in range(len(logs))]
    ends = [logs[i][1] for i in range(len(logs))]
    starts.sort()
    ends.sort()
    starts_index, ends_index = 0, 0
    to_add = 0
    i = 0
    while i < play_time + 1:
        if starts_index <= len(logs) - 1 and starts[starts_index] == i:
            to_add += 1
            starts_index += 1
        if ends_index <= len(logs) - 1 and ends[ends_index] == i:
            to_add -= 1
            ends_index += 1
        counts[i] = to_add

        if (starts_index <= len(logs) - 1 and starts[starts_index] == i) or (ends_index <= len(logs) - 1 and ends[ends_index] == i):
            continue
        i += 1

    cur_sum = sum(counts[:adv_time])
    max_sum = cur_sum
    max_sum_index = 0
    for i in range(adv_time, play_time+1):
        cur_sum -= counts[i-adv_time]
        cur_sum += counts[i]

        if max_sum < cur_sum:
            max_sum = cur_sum
            max_sum_index = i - adv_time + 1
            
    answer = convert_to_hhmmss(max_sum_index)
    return answer

play_time = str(input().rstrip())
adv_time = str(input().rstrip())
N = int(input())
logs = [input().rstrip() for _ in range(N)]
print(solution(play_time, adv_time, logs))