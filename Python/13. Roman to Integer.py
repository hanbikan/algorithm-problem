symbol = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
class Solution:
    def romanToInt(self, s):
        RET = 0
        for i in range(len(s)-1):
            if symbol[s[i]]<symbol[s[i+1]]:
                RET -= symbol[s[i]]
            else:
                RET += symbol[s[i]]
        RET += symbol[s[len(s)-1]]
        return RET
Input = 'MCMXCIV'
s = Solution()
print(s.romanToInt(Input))