class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        max_sum = 0

        for R in range(len(prices)):
            if prices[L] <= prices[R]:
                cur_sum = prices[R] - prices[L]
                max_sum = max(max_sum, cur_sum)
        

            else:
                L = R

                            
    
            
        return max_sum
