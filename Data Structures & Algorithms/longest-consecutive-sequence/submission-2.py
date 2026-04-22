class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my = set(nums)
        ans = 0

        for i in nums:
            if (i-1) not in my:
                length = 0
                while (i + length) in my:
                    length += 1
                ans = max(ans, length)
        return ans