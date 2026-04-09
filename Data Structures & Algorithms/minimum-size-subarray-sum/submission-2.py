class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        tot = 0
        length = float("inf")

        for right in range(len(nums)):
            tot += nums[right]

            while tot >= target:
                length = min(length, right-left+1)
                tot -= nums[left]
                left += 1 
        return 0 if length == float("inf") else length