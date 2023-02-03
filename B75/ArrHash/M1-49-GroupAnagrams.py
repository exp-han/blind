from collections import defaultdict
# Solution 1 - Using Tuples & Dictionary
# Comments:
#   - Need to review about tuples, basic python functions
# TODO:
#   - Review tuples, python builtin functions
#   - Look for possible better solutions
class Solution1:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        sdict = defaultdict(list) # key = tuple, value = array
        for s in strs:
            sdict[tuple(sorted(s))].append(s)
        return sdict.values()