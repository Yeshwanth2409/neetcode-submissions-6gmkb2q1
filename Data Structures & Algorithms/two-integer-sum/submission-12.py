class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        amp = {}
        for i,j in enumerate(nums):
            comp = target - j
            if comp in amp:
                return [amp[comp], i]
            else:
                amp[j] = i