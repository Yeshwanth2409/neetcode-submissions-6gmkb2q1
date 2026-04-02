class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        ans = 0

        for R in range(len(prices)):
            if prices[L] <= prices[R]:
                res = prices[R] - prices[L]
                ans = max(ans, res)

            else:
                L = R
        return ans
