import sys
input = sys.stdin.readline

factorials = {0:1, 1:1}

def getFactorial(n):
    if factorials.get(n):     
        return factorials[n]
      
    res = getFactorial(n-1)*n
    factorials[n] = res
    return res

def getCombination(n, r):
    return getFactorial(n) / (getFactorial(n-r) * getFactorial(r))

# P(X=n)
def calculateProbability(percentage, n):
    return getCombination(18, n)*(percentage**n)*((1-percentage)**(18-n))

def solution(A, B):
    pa = A/100
    pb = B/100
    
    resA = 0
    resB = 0
    for num in 0,1,4,6,8,9,10,12,14,15,16,18:      
        resA += calculateProbability(pa, num)
        resB += calculateProbability(pb, num)

    # 1 - (A¿Í B ¸ðµÎ ¼Ò¼ö°¡ ¾Æ´Ò È®·ü)
    print(1 - resA * resB)

if __name__ == '__main__':
    A = int(input())
    B = int(input())
    solution(A, B)