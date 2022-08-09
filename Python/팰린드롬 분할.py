import sys
sys.setrecursionlimit(200000)

input = sys.stdin.readline
NOT_INITIALIZED, TRUE, FALSE = 0, 1, 2


def getMinCount():
    todo = [0]

    for c in range(input_len+1):
        nextTodo = []

        while todo:
            start = todo.pop(0)

            if start >= input_len:
                return c

            for e in range(input_len-1, start-1, -1):
                if setIsPalindrome(start, e) == TRUE and c+1 < dp[e+1]:
                    dp[e+1] = c + 1
                    nextTodo.append(e+1)

        todo = nextTodo


def setIsPalindrome(start, end):
    # Base case
    if start >= end:
        isPalindrome[start][end] = TRUE
        return TRUE

    # Recursive case
    if input_str[start] != input_str[end]:
        isPalindrome[start][end] = FALSE
        return FALSE

    # 초기화
    if isPalindrome[start][end] == NOT_INITIALIZED:
        isPalindrome[start][end] = setIsPalindrome(start+1, end-1)

    return isPalindrome[start][end]


if __name__ == '__main__':
    # 입력
    input_str = str(input().rstrip())
    input_len = len(input_str)

    # 처리
    dp = [input_len+1]*(input_len+1)
    isPalindrome = [[NOT_INITIALIZED]*input_len for _ in range(input_len)]

    minCount = getMinCount()

    # 출력
    print(minCount)
