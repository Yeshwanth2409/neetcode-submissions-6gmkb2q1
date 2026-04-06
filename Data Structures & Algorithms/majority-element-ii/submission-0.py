class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        hmp = {}

        for i in range(len(nums)):
            if nums[i] in hmp:
                hmp[nums[i]] += 1

            else:
                hmp[nums[i]] = 1

        for key, value in hmp.items():
            if value > len(nums)/3:
                res.append(key)

        return res
