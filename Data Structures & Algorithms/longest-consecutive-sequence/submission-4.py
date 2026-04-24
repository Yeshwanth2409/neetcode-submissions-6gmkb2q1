class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x = set(nums)
        tot = 0

        for i in nums:
            if (i-1) not in x:
                length = 0
                while (i+length) in x:
                    length += 1
                tot = max(tot, length)
        return tot
            