class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        L = [0] * len(temperatures)
        stack = []
        
        for R in range(len(temperatures)):
            while stack and temperatures[R] > temperatures[stack[-1]]:
                idx = stack.pop()
                L[idx] = R - idx
            stack.append(R)

        return L
            

