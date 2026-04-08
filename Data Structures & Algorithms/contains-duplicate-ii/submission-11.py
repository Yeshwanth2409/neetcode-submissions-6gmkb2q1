class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for L in range(len(nums)):
        #     for R in range(L, min(len(nums), L+k)):
        #         if nums[L] == nums[R]:
        #             return True
                
        #     return False
        window = set()
        L = 0

        for R in range(len(nums)):
            if R-L > k:
                window.remove(nums[L])
                L += 1
            
            if nums[R] in window:
                return True
            
            window.add(nums[R])
        
        return False