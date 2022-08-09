import sys
input = sys.stdin.readline


def dfs(count):
    global minButtonClickCount, selectedDigits

    if (len(str(N))-1 <= count <= len(str(N))+1) and selectedDigits != []:
        targetChannel = convertDigitsToNumber(selectedDigits)
        channelDiff = abs(targetChannel-N)

        minButtonClickCount = min(
            minButtonClickCount, channelDiff+len(str(targetChannel)))

    if count == len(str(N))+1:
        return

    for i in range(10):
        if isAvailableDigit[i]:
            selectedDigits.append(i)
            dfs(count+1)
            selectedDigits.pop()


def convertDigitsToNumber(digits):
    convertedNumber = 0

    j = 0
    for i in range(len(digits)-1, -1, -1):
        convertedNumber += digits[i]*10**j
        j += 1

    return convertedNumber


isAvailableDigit = [True]*10

N = int(input())
M = int(input())
if M >= 1:
    for i in list(map(int, input().split())):
        isAvailableDigit[i] = False

# +-만으로 이동
minButtonClickCount = abs(N-100)

if M <= 9:
    # 가장 가까운 채널 입력 -> +- 입력
    selectedDigits = []
    dfs(0)

print(minButtonClickCount)
