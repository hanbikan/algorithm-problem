def get_factorial(n):
    if n <= 1:
        return 1
    return n*get_factorial(n-1)


def get_combination(n, k):
    return get_factorial(n) // (get_factorial(k)*get_factorial(n-k))


if __name__ == '__main__':
    N, K = map(int, input().split())
    print(get_combination(N, K))
