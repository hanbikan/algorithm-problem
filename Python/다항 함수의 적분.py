import sys
input = sys.stdin.readline

class Elem:
    def __init__(self, a, b): #ax^b
        self.a = a
        self.b = b

# -3xx -> -3x^2
def parse_string_as_elem(string):
    is_positive = True
    if string[0] == '-':
        is_positive = False

    start_number_index = 0
    if string[0] == '+' or string[0] == '-':
        start_number_index = 1

    start_x_index = find_index(string, 'x')
    if start_x_index == -1:
        a = int(string)
        return Elem(a, 0)
    else:
        a = int(string[start_number_index:start_x_index])
        if not is_positive: a *= -1
        return Elem(a,len(string) - start_x_index)

def find_index(string, char):
    for i in range(len(string)):
        if string[i] == char:
            return i

    return -1

def integral_elem(elem: Elem):
    elem.a /= elem.b+1
    elem.b += 1
    return elem

def print_elem(elem: Elem, should_print_sign):
    if(should_print_sign and elem.a>0): print("+",end="")
    if(elem.a == -1):
        if(elem.b == 0):
            print("-1",end="")
        else:
            print("-",end="")
    elif(elem.a != 1):
        print(int(elem.a), end="")
    print('x'*elem.b,end="")

if __name__ == '__main__':
    string = str(input().rstrip())
    if(string == "0"):
        print("W")
    else:
        cur = ""
        should_print_sign = False
        for c in string:
            if cur != "" and c == '-' or c == '+':
                elem = parse_string_as_elem(cur)
                print_elem(integral_elem(elem), should_print_sign)
                should_print_sign = True
                cur = ""
            cur += c

        elem = parse_string_as_elem(cur)
        print_elem(integral_elem(elem), should_print_sign)
        print("+W",end="")