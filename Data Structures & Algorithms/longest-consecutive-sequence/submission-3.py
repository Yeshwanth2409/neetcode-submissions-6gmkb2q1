class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        ans = 0

        for i in nums:
            if (i-1) not in mySet:
                length = 0
                while (length + i) in mySet:
                    length += 1
                ans = max(length, ans)
        return ans