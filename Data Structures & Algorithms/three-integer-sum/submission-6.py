class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # [-3,-3,1,2,3,3]
        for i,j in enumerate(nums):
            if i > 0 and j == nums[i-1]:
                continue

            L = i + 1
            R = len(nums) - 1

            while L < R:
                ans = j + nums[L] + nums[R]
                if ans > 0:
                    R -= 1
                elif ans < 0:
                    L += 1
                else:
                    res.append([j, nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
        return res


        