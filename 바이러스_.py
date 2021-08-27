import sys
input = sys.stdin.readline


def get_pi(keyword):
    keyword_length = len(keyword)
    pi = [0]*keyword_length
    j = 0

    for i in range(1, keyword_length):
        while j > 0 and keyword[i] != keyword[j]:
            j = pi[j-1]

        if keyword[i] == keyword[j]:
            j += 1
            pi[i] = j

    return pi


def it_there_one_keyword(string, keyword, pi):
    string_length = len(string)
    i, j = 0, 0

    while i < string_length:
        if string[i] == keyword[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = pi[j-1]

        if j == K:
            return True

    return False


def has_virus():
    for i in range(K, len(info[0])+1):
        # Set target
        cur_str = info[0][i-K:i]
        cur_str_reversed = list(reversed(cur_str))

        # Search
        flag = True
        pi = get_pi(cur_str)
        pi_reversed = get_pi(cur_str_reversed)

        for j in range(1, N):
            result1 = it_there_one_keyword(info[j], cur_str, pi)
            result2 = it_there_one_keyword(info[j], cur_str_reversed, pi_reversed)

            if result1 == False and result2 == False:
                flag = False
                break

        # If keyword was searched in every other strings
        if flag:
            return True

    return False


if __name__ == '__main__':
    N, K = map(int, input().split())

    info = []
    for _ in range(N):
        _ = int(input())
        info.append(list(map(int, input().split())))

    if(has_virus()):
        print("YES")
    else:
        print("NO")
