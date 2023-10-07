import sys
input = sys.stdin.readline

def permutation(index):
    if index >= N:
        current_left_teller_counts = [0] * N
        for i in range(N):
            left_teller_count = 0
            for left_index in range(i):
                if numbers[left_index] > numbers[i]:
                    left_teller_count += 1
            current_left_teller_counts[numbers[i] - 1] = left_teller_count
        return left_teller_counts == current_left_teller_counts

    for i in range(1, N + 1):
        if i in used: continue
        numbers[index] = i
        used.add(i)
        if permutation(index + 1):
            return True
        used.remove(i)

N = int(input())
left_teller_counts = list(map(int,input().split()))

current_left_teller_counts = [0] * N
numbers = [0] * N
used = set()

permutation(0)
print(*numbers)