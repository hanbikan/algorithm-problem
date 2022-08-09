import sys
input = sys.stdin.readline

trees = {}
treeCount = 0

while True:
    curInput = input().rstrip()
    if not curInput:
        break

    if trees.get(curInput):
        trees[curInput] += 1
    else:
        trees[curInput] = 1
    treeCount += 1

sortedTreesName = sorted(trees.keys())
for treeName in sortedTreesName:
    print('%s %.4f' % (treeName, trees[treeName]*100/treeCount))
