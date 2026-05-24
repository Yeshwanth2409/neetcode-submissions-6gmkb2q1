class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        amp = {}
        for i in nums:
            if i not in amp:
                amp[i] = 1
            else:
                amp[i] += 1
        
        heap = []
        for num in amp.keys():
            heapq.heappush(heap, (amp[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res