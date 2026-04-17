class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        amp = {}
        cam = {}
        for i in s:
            if i not in amp:
                amp[i] = 1
            else:
                amp[i] += 1
        
        for j in t:
            if j not in cam:
                cam[j] = 1
            else:
                cam[j] += 1

        if amp == cam:
            return True
        else:
            return False