class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        profit = 0
        min_num = nums[0]

        for i in nums:
            profit = max(profit, i - min_num)
            min_num = min(min_num, i)

        return profit