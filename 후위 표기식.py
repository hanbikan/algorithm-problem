import sys
input = sys.stdin.readline


def getPriorty(c):
    if c >= 'A' and c <= 'Z':
        return 0
    elif c == '(' or c == ')':
        return 1
    elif c == '*' or c == '/':
        return 2
    elif c == '+' or c == '-':
        return 3
    else:
        return -1


if __name__ == '__main__':
    infixNotation = str(input().rstrip())

    postfixNotation = []
    stack = []

    for c in infixNotation:
        priority = getPriorty(c)

        # 문자열
        if priority == 0:
            postfixNotation.append(c)
        # ()
        elif priority == 1:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if stack:
                    cur = stack[-1]
                    # 괄호가 끝날 때까지, 스택을 모두 꺼냄
                    while stack and cur != '(':
                        cur = stack.pop()
                        postfixNotation.append(cur)
        # */+-
        else:
            # 스택이 비었거나, 현재의 우선순위가 높을 경우
            if len(stack) == 0 or getPriorty(stack[-1]) > priority:
                stack.append(c)
            else:
                # 우선순위가 더 높은 스택들을 모두 꺼냄
                while stack and stack[-1] != '(' and getPriorty(stack[-1]) <= priority:
                    postfixNotation.append(stack.pop())
                stack.append(c)

    # 남아있는 모든 스택을 꺼냄
    while stack:
        postfixNotation.append(stack.pop())

    # 출력
    for c in postfixNotation:
        if c != '(':
            print(c, end="")
