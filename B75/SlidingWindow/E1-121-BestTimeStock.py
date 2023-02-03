# Solution 1 - Naive SWindow
# Date: 02/02/23
# Time: 03' 20"
# Comment:
#   - Better Sol?
class Solution1:
    def maxProfit1(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        l, r = 0, 1
        maxprofit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                maxprofit = max(maxprofit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxprofit