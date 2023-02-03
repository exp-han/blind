from collections import Counter
# Solution 1 - Using Counter
# Comments:
#   - Neet to try without Counter class
#   - Need to be handy with using Counter class
class Solution1:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        return [int(num[0]) for num in Counter(nums).most_common(k)]

# Solution 2 - Without using Counter
# Comment:
#   - Review python default sorting functions
#   - Look for possible better solution
# TODO:
#   - Find better solution
class Solution2:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        ndict = dict()
        for num in nums:
            ndict[num] = 1 + ndict.get(num, 0)
        ndict_sorted = sorted(ndict.items(), key=lambda x: x[1], reverse=True)[:k]
        return [int(n[0]) for n in ndict_sorted]