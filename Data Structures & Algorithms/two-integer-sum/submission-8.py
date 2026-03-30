class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pam = {}
        for i, j in enumerate(nums):
            comp = target - j
            if comp in pam:
                return [pam[comp], i]
            pam[j] = i