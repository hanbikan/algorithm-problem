class NodeTree:
    def __init__(self, val):
        self.val=val
        self.next=[]
        self.to=None

def linkNodes(n1, n2):
    n1.next.append(n2)
    n2.next.append(n1)

def getMaxDP(node, DP):
    maxval = 0
    maxNode = None
    nextnext = getNextNodesFromNodes(node.next, [node])
    for j in range(len(nextnext)):
        if nextnext[j].val > maxval:
            maxval = nextnext[j].val
            maxNode = nextnext[j]
    nextnextnext = []
    for j in range(len(nextnext)):
        nextnextnext+=getNextNodesFromNodes([nextnext[j]], [nextnext[j]]+node.next)
    for j in range(len(nextnextnext)):
        if nextnextnext[j].val > maxval:
            maxval = nextnextnext[j].val
            maxNode = nextnextnext[j]

    if maxNode: maxNode.to = node
    return maxNode

def getNextNodesFromNodes(nodes, blackList):
    RET = []
    for i in range(len(nodes)):
        for j in range(len(nodes[i].next)):
            for k in range(len(blackList)):
                if blackList[k]==nodes[i].next[j]:
                    k=-1
                    break
            if k!=-1: RET.append(nodes[i].next[j])
    return RET

towns=[NodeTree(1000), NodeTree(3000), NodeTree(4000), NodeTree(1000), NodeTree(2000), NodeTree(2000), NodeTree(7000)]
linkNodes(towns[0], towns[1])
linkNodes(towns[1], towns[2])
linkNodes(towns[3], towns[2])
linkNodes(towns[3], towns[4])
linkNodes(towns[5], towns[1])
linkNodes(towns[5], towns[6])

DP = [NodeTree(0) for i in range(7)]
linkNodes(DP[0], DP[1])
linkNodes(DP[1], DP[2])
linkNodes(DP[3], DP[2])
linkNodes(DP[3], DP[4])
linkNodes(DP[5], DP[1])
linkNodes(DP[5], DP[6])

for i in range(7):
    maxNode = getMaxDP(DP[i], DP)
    if maxNode:
        if maxNode.to!=DP[i]:
            while maxNode.to:
                print("!")
                maxNode=maxNode.to
        DP[i].val = maxNode.val + towns[i].val
    else: DP[i].val = towns[i].val
    print(DP[i].val)

for i in range(7):
    if DP[i].to: print(i, DP[i].to.val)