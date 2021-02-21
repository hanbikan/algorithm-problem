class Solution:
	def maxProfit(self, prices):
		if len(prices) <= 1: return 0
		s0 = [0 for i in range(len(prices))]
		s1 = [0 for i in range(len(prices))]
		s2 = [0 for i in range(len(prices))]
		s0[0] = -prices[0]
		s1[0] = 0
		s2[0] = 0
		for i in range(1, len(prices)):
			s0[i] = max(s0[i-1], s2[i-1])
			s1[i] = max(s1[i-1], s0[i-1]-prices[i])
			s2[i] = s1[i-1] + prices[i]
		return max(s0[len(prices)-1], s2[len(prices)-1])
		
prices = [1,2,3,0,2]
s = Solution()
print(s.maxProfit(prices))