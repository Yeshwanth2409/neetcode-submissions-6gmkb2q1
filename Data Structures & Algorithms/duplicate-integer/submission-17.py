class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = []

        for num in nums:
            if num in x:
                return True
            x.append(num)
        return False