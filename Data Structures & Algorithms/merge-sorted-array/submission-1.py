class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m+n-1
        L = m-1
        R = n-1

        while L >= 0 and R >= 0:
            if nums1[L] > nums2[R]:
                nums1[last] = nums1[L]
                L -= 1
            else:
                nums1[last] = nums2[R] 
                R -= 1
            last -= 1

        while R >= 0:
            nums1[last] = nums2[R]
            R, last = R-1, last-1
