class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        tot = 0
        for i in nums:
            tot += i
            self.prefix.append(tot)

        

    def sumRange(self, left: int, right: int) -> int:
        right_p = self.prefix[right]
        left_p = self.prefix[left-1] if left > 0 else 0
        return right_p - left_p
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)