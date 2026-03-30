class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        max_sub = 0
        amp = set()

        for R in range(len(s)):
            while s[R] in amp:
                amp.remove(s[L])
                L += 1
            
            amp.add(s[R])

            max_sub = max(max_sub, R-L+1)

        return max_sub