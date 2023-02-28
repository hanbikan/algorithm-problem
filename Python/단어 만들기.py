import sys
input = sys.stdin.readline

words = []
while True:
    word = str(input().rstrip())
    if word == '-':
        break
    words.append(word)

while True:
    puzzle = str(input().rstrip())
    if puzzle == '#':
        break

    counts = [0] * 26
    for c in puzzle:
        counts[ord(c) - ord('A')] += 1
    
    
    answers = [0] * 26
    for word in words:
        is_answer = True
        counts_for_word = [0] * 26
        for c in word:
            counts_for_word[ord(c) - ord('A')] += 1
        
        for i in range(26):
            if counts[i] < counts_for_word[i]:
                is_answer = False
                break
        
        if is_answer:
            added = set()
            for c in word:
                if c not in added:
                    answers[ord(c) - ord('A')] += 1
                    added.add(c)
        
    minn = float('inf')
    for c in puzzle:
        minn = min(minn, answers[ord(c) - ord('A')])
    maxx = max(answers)

    min_chars = set()
    max_chars = set()
    for c in puzzle:
        if answers[ord(c) - ord('A')] == minn:
            min_chars.add(c)
        if answers[ord(c) - ord('A')] == maxx:
            max_chars.add(c)
    
    min_chars = sorted(list(min_chars))
    max_chars = sorted(list(max_chars))
    for c in min_chars:
        print(c, end="")
    print(" {0}".format(minn), end=" ")
    for c in max_chars:
        print(c, end="")
    print(" {0}".format(maxx))