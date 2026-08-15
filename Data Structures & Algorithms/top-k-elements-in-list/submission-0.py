from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr=Counter(nums).most_common(k)
        return [item for item, _ in ctr]
        