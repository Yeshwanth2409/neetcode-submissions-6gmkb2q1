class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        amp = {}
        for i in nums:
            if i not in amp:
                amp[i] = 1
            else:
                amp[i] += 1
        
        return max(amp, key=amp.get)
             