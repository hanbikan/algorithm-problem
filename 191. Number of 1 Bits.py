class Solution:
    def hammingWeight(self, n):
        c = 0
        while n:
            print(bin(n))
            n &= n - 1
            c += 1
        return c

Input = 0b11111111111111111111111111111101
s = Solution()
print(s.hammingWeight(Input))