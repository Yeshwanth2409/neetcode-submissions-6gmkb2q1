class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s = set(nums)
        best = 0

        for x in s:
            if (x-1) not in nums:
                current = x
                length = 1

                while (current + 1) in s:
                    current += 1
                    length += 1

                if length > best:
                    best = length

        return best    