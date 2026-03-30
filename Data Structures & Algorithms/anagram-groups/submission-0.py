class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for words in strs:
            count = [0] * 26
            for char in words:
                count[ord(char) - ord('a')] += 1
            group[tuple(count)].append(words)
        return list(group.values())  