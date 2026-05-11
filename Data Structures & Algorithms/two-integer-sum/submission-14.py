class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        amp = {}
        for i,j in enumerate(nums):
            diff = target - j
            if diff in amp:
                return [amp[diff], i]
            amp[j] = i