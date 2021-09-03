import sys
input = sys.stdin.readline


def solution():
    primes = get_prime_numbers()

    # Two pointers
    count = 0
    primes_length = len(primes)

    start = 0
    cur_sum = 0
    for i in range(primes_length):
        # 현재 값을 추가
        cur_sum += primes[i]

        # N 이하가 될 때까지 감소시킴
        while cur_sum > N:
            cur_sum -= primes[start]
            start += 1

        # 그 결과가 N과 같을 시
        if cur_sum == N:
            count += 1

    return count


def get_prime_numbers():
    prime_numbers = []
    dp = [True]*(N+1)

    for i in range(2, N+1):
        if dp[i] == True:
            prime_numbers.append(i)

            for j in range(i*2, N+1, i):
                dp[j] = False

    return prime_numbers


if __name__ == '__main__':
    N = int(input())

    print(solution())
