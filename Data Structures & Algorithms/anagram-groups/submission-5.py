from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gans = defaultdict(list)
        for s in strs:
            # each char in string has its own counter
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            gans[tuple(count)].append(s)
        return list(gans.values())
    

