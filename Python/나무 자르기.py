def getSmallerSumMeterIndex(sumMeter, m):
    left, right = 0, len(sumMeter)-1
    while left < right:
        mid = (right + left)//2
        if sumMeter[mid] < m:
            right = mid
        elif sumMeter[mid] > m:
            left = mid + 1
        elif sumMeter[mid] == m:
            return mid
    return left

N, M = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()

sumMeter = []
for i in range(N):
    if i==0:
        additionalCutHeight = heights[0]
        prevSumMeter = sum(heights)
    else:
        additionalCutHeight = heights[i]-heights[i-1]
        prevSumMeter = sumMeter[i-1]
    sumMeter.append(prevSumMeter-additionalCutHeight*(N-i))

idx = getSmallerSumMeterIndex(sumMeter, M)
plus = N-idx
curMeter = sumMeter[idx]
curHeight = heights[idx]
if (M-curMeter)/plus == (M-curMeter)//plus:
    print(curHeight-(M-curMeter)//plus)
else:
    print(curHeight-(M-curMeter)//plus-1)