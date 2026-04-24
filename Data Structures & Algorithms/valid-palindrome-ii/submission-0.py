class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def pal(L, R):
            while L < R:
                if s[L] != s[R]:
                    return False
                L, R = L+1, R-1
            return True

        L = 0
        R = len(s) - 1

        while L < R:
            if s[L] != s[R]:
                return pal(L+1,R) or pal(L,R-1)

            L, R = L+1, R-1
        return True