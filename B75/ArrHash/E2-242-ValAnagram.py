from collections import Counter
# Solution 1 - Using Counter class
# Comments:
#   - Need to be handy with using Counter class
#   - Need to be aware of the parameter types for dict & return type for dict related functions
#   - Need to be handy with using lambda functions
# TODO:
#   - Read Counter, dict docs
#   - Practice on lambda functions
class Solution1:
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sdict, tdict = dict(Counter(s).most_common()), dict(Counter(t).most_common())
        sdict, tdict = sorted(sdict.items(), key=lambda item: (item[1], item[0])), sorted(tdict.items(), key=lambda item: (item[1], item[0]))
        for sc, tc in zip(sdict, tdict):
            if sc[0] != tc[0] or sc[1] != tc[1]:
                return False
        return True

# Solution 2 - Sort string & Iterate
# Comments:
#   - Neet to review handling strings
# TODO:
#   - Look for better solution
class Solution2:
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        slst, tlst = list(c for c in s), list(c for c in t)
        slst.sort()
        tlst.sort()
        for i in range(len(slst)):
            if slst[i] != tlst[i]:
                return False
        return True