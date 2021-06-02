import sys
input = sys.stdin.readline


def isValidIndex(index):
    for i in range(wordLen):
        if document[index+i] != word[i]:
            return False

    return True


document = str(input().rstrip())
word = str(input().rstrip())
documentLen, wordLen = len(document), len(word)

count = 0
i = 0
while i < documentLen-wordLen+1:
    if isValidIndex(i):
        count += 1
        i += wordLen
    else:
        i += 1

print(count)
