class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        ans = 0

        for R in range(1, len(prices)):
            if prices[R] > prices[R-1]:
                ans += prices[R] - prices[R-1]

        return ans