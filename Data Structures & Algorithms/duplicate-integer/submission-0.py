class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Hash set to store elements we've seen
        for num in nums:
            if num in seen:   # Duplicate found
                return True
            seen.add(num)     # Add number to set
        return False  