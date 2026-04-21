class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # amp = {}
        # for i in nums:
        #     if i not in amp:
        #         amp[i] = 1
        #     else:
        #         amp[i] += 1
        
        # return max(amp, key=amp.get)
        res = 0
        count = 0

        for i in nums:
            if count == 0:
                res = i
            if i == res:
                count += 1
            else:
                count -= 1
        return res
             