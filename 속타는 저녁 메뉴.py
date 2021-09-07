import sys
input = sys.stdin.readline


def get_pi(keyword):
    keyword_length = len(keyword)
    pi = [0]*keyword_length

    j = 0
    for i in range(1, keyword_length):
        while keyword[i] != keyword[j] and j > 0:
            j = pi[j-1]

        if keyword[i] == keyword[j]:
            j += 1
            pi[i] = j

    return pi


def find_keyword(string, keyword):
    keyword_count = 0
    string_length = len(string)
    keyword_lenght = len(keyword)

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

        if j == keyword_lenght:
            keyword_count += 1
            j = pi[j-1]

    return keyword_count


if __name__ == '__main__':
    N = int(input())
    target = list(map(str, input().split()))
    roulette = list(map(str, input().split()))
    roulette += roulette[:-1]

    # KMP를 통해 target의 갯수를 가져옴
    pi = get_pi(target)
    target_count = find_keyword(roulette, target)

    # 최대공약수를 찾은 뒤, 여기에 맞추어 출력함
    for i in range(target_count, 0, -1):
        if target_count % i == 0 and N % i == 0:
            print("{0}/{1}".format(target_count//i, N//i))
            break
