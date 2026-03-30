class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)

    # Step 2: Create buckets (index = freq)
        bucket = [[] for _ in range(len(nums)+1)]
        for num, freq in freq_map.items():
            bucket[freq].append(num)

        # Step 3: Gather top k from buckets
        result = []
        for freq in range(len(bucket)-1, 0, -1):
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result
