class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        res = R

        while L <= R:
            k = (L+R)//2
            hours = 0
            for i in piles:
                hours += math.ceil(float(i)/k)

            if hours > h:
                L = k + 1
            
            else:
                res = min(res, k)
                R = k - 1
        return res
             
            
                

       
            

