class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for i in nums:
            count[i] += 1

        n = 0
        for i in range(len(count)):
            for j in range(count[i]):
                nums[n] = i
                n += 1
        return nums

        