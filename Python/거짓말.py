import sys
input = sys.stdin.readline


def visitPartyKnowledgeablePeoplepartyToAttend():
    for ppl in range(1, N+1):
        if isPeopleKnowledgeable[ppl] == True:
            for pty in partyToAttend[ppl]:
                if isPartyKnowledgeable[pty] == False:
                    setIsPartyKnowledgeableTrue(pty)


def setIsPartyKnowledgeableTrue(party):
    isPartyKnowledgeable[party] = True
    for ppl in partyPeople[party]:
        isPeopleKnowledgeable[ppl] = True

        for pty in partyToAttend[ppl]:
            if isPartyKnowledgeable[pty] == False:
                setIsPartyKnowledgeableTrue(pty)


def getUnknowledgeablePartyCount():
    unknowledgeablePartyCount = 0

    for i in range(M):
        if isPartyKnowledgeable[i] == False:
            unknowledgeablePartyCount += 1

    return unknowledgeablePartyCount


if __name__ == '__main__':
    N, M = map(int, input().split())

    isPeopleKnowledgeable = [False]*(N + 1)
    curNums = list(map(int, input().split()))
    for i in range(1, curNums[0] + 1):
        isPeopleKnowledgeable[curNums[i]] = True

    partyPeople = []
    partyToAttend = [[] for _ in range(N + 1)]

    for i in range(M):
        curNums = list(map(int, input().split()))

        partyPeople.append(curNums[1:])
        for j in range(1, curNums[0] + 1):
            partyToAttend[curNums[j]].append(i)

    isPartyKnowledgeable = [False]*M

    visitPartyKnowledgeablePeoplepartyToAttend()

    unknowledgeablePartyCount = getUnknowledgeablePartyCount()
    print(unknowledgeablePartyCount)
