import sys
input = sys.stdin.readline


def get_pi(keyword):
    keyword_length = len(keyword)
    pi = [0]*keyword_length

    i, j = 1, 0
    for i in range(1, keyword_length):
        while(keyword[i] != keyword[j] and j > 0):
            j = pi[j-1]

        if(keyword[i] == keyword[j]):
            j += 1
            pi[i] = j

    return pi


def doKMP(string, keyword):
    count = 0
    indices = []

    pi = get_pi(keyword)

    string_length = len(string)
    keyword_length = len(keyword)

    i, j = 0, 0
    while(i < string_length):
        if(string[i] == keyword[j]):
            i += 1
            j += 1
        else:
            if(j > 0):
                j = pi[j-1]
            else:
                i += 1

        if(j == keyword_length):
            j = pi[j - 1]

            count += 1
            indices.append(i-keyword_length+1)

    return count, indices


if __name__ == '__main__':
    T = str(input().rstrip())
    P = str(input().rstrip())

    count, indices = doKMP(T, P)
    print(count)
    print(*indices)
