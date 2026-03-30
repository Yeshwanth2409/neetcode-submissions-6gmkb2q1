class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        L = 0
        R = len(heights) - 1

        while L < R:
            if heights[L] < heights[R]:
                area = min(heights[L], heights[R]) * (R-L)
                ans = max(ans, area)
                L += 1
            
            else:
                area = min(heights[L], heights[R]) * (R-L)
                ans = max(ans, area)
                R -= 1
        return ans

        