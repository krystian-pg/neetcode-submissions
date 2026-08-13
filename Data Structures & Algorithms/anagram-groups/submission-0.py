from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for _, string in enumerate(strs):
            key = frozenset(Counter(string).items())
            anagrams[key].append(string)
        return list(anagrams.values())
        