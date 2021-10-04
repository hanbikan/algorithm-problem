import sys
input = sys.stdin.readline


def get_measures(n):
    res = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            res.add(i)
            res.add(n//i)

    res.remove(1)

    return res


def gcd(x, y):
    if y != 0:
        return gcd(y, x % y)
    else:
        return x


if __name__ == '__main__':
    N = int(input())
    nums = list(int(input()) for _ in range(N))
    nums.sort()

    g = nums[1] - nums[0]
    for i in range(1, N-1):
        g = gcd(g, nums[i+1] - nums[i])

    print(*sorted(list(get_measures(g))))
