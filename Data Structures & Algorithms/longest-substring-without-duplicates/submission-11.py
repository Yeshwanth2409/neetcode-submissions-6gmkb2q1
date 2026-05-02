class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        sub = set()
        ans = 0

        for R in range(len(s)):
            while s[R] in sub:
                sub.remove(s[L])
                L += 1
            
            sub.add(s[R])
            ans = max(ans, R-L+1)
        return ans
            
