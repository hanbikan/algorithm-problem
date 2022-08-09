N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))

stack = []
toPush = 1
toPrint = []
for num in nums:
    while toPush <= num:
        toPrint.append("+")
        stack.append(toPush)
        toPush += 1

    if stack.pop() == num:
        toPrint.append("-")
    else:
        toPrint = ["NO"]
        break

for c in toPrint:
    print(c)
