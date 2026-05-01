class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(k):
            L = 0
            R = len(nums) - 1
            tmp = nums[R]
            while L < R:
                nums[R] = nums[R-1]
                R -= 1 
            
            nums[L] = tmp