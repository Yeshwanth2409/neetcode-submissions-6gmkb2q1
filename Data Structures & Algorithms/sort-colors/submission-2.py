class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for i in nums:
            count[i] += 1

        n = 0
        for x in range(len(count)):
            for y in range(count[x]):
                nums[n] = x
                n += 1
        return nums 

        