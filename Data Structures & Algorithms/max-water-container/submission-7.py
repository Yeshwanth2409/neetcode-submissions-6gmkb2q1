class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        L = 0
        R = len(heights) - 1

        while L < R:
            area = min(heights[L], heights[R]) * (R-L)
            if heights[L] >= heights[R]:
                R -= 1
            else:
                L += 1
            ans = max(ans, area)
        return ans


        