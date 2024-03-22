import sys
input = sys.stdin.readline

weights = {'H': 1, 'C': 12, 'O': 16}

def get_weight(start, end):
    result = 0

    i = start
    while i < end:
        c = formula[i]
        
        if c == 'H' or c == 'C' or c == 'O':
            if i + 1 < end and '2' <= formula[i + 1] <= '9': # H2
                result += weights[c] * int(formula[i + 1])
                i += 2
            else: # CH
                result += weights[c]
                i += 1
        else: # assume '('
            next_start = i + 1
            next_end = next_start
            stack = 1
            while next_end < end:
                if formula[next_end] == ')':
                    stack -= 1
                elif formula[next_end] == '(':
                    stack += 1
                if stack == 0:
                    break
                next_end += 1
            
            if next_end + 1 < end and '2' <= formula[next_end + 1] <= '9':
                result += get_weight(next_start, next_end) * int(formula[next_end + 1])
            else:
                result += get_weight(next_start, next_end)
            
            i = next_end + 1
    return result

formula = str(input().rstrip())
print(get_weight(0, len(formula)))