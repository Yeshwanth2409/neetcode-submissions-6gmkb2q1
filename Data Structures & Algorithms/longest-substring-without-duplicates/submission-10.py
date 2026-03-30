class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        res = 0
        amp = set()

        for R in range(len(s)):
            while s[R] in amp:
                amp.remove(s[L])

                L += 1

            amp.add(s[R])

            res = max(res, R-L+1)
        return res
