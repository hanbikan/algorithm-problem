import sys
input = sys.stdin.readline


def get_pi(string):
    string_length = len(string)
    pi = [0]*string_length
    j = 0

    for i in range(1, string_length):
        while j > 0 and string[i] != string[j]:
            j = pi[j-1]

        if string[i] == string[j]:
            j += 1
            pi[i] = j

    return pi


if __name__ == '__main__':
    L = int(input())
    S = str(input().rstrip())

    pi = get_pi(S)
    print(L - pi[-1])
