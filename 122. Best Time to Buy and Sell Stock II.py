class Solution:
    def maxProfit(self, prices):
        profit = 0
        i=0
        while i<len(prices):
            upstair_end = self.get_upstair_end(prices, i)
            if upstair_end > i:
                profit += prices[upstair_end]-prices[i]
                i = upstair_end
            i+=1
        print(profit)
        return profit
    def get_upstair_end(self, prices, idx):
        lp = len(prices)
        if idx == lp-1: return idx
        for i in range(idx, lp-1):
            if prices[i] > prices[i+1]:
                break
        if i == lp-2 and prices[lp-2] < prices[lp-1]:
            return lp-1
        return i
prices = [7,6,4,3,1]
s = Solution()
s.maxProfit(prices)