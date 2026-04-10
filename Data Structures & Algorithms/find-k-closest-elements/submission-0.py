class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        amp = []
        for i in arr:
            diff = abs(i-x)
            amp.append((diff, i))
        
        res = sorted(amp)[:k]
        return sorted([val for diff, val in res])