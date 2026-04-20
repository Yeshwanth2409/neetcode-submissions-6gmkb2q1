class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        amp = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j) - ord('a')] += 1
            amp[tuple(count)].append(i)
        return list(amp.values())