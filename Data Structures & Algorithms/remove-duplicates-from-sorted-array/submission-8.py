class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = []
        for i in nums:
            if i in x:
                continue
            else:
                x.append(i)
        nums[:len(x)] = x
        return len(x)