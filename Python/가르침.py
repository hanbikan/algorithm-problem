import sys
input = sys.stdin.readline


def dfs(idx, cnt):
    global maxCntReadable
    if cnt == K-5:  # Base Case
        cntReadable = 0
        for word in words:
            isReadable = True
            for c in word:
                if isLearned[ord(c)-ord('a')] == False:
                    isReadable = False
                    break
            if isReadable:
                cntReadable += 1
        maxCntReadable = max(maxCntReadable, cntReadable)
        return

    for i in range(idx, 26):  # Recursive Case
        if isLearned[i] == False:
            isLearned[i] = True
            dfs(i, cnt+1)
            isLearned[i] = False


N, K = map(int, input().split())
words = [input().strip() for _ in range(N)]

if K < 5:
    print(0)
else:
    isLearned = [False]*26

    for c in ('a', 'c', 'i', 'n', 't'):
        isLearned[ord(c)-ord('a')] = True

    maxCntReadable = -1
    dfs(0, 0)
    print(maxCntReadable)
