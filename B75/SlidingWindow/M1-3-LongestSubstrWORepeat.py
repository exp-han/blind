# Solution 1 - Naive Shrink/Expand SWindow
# Date: 02/02/23
# Time: 08' 45"
# Comment:
#   - Thought Process 좀 더 차근차근 할 것
#   - 연습 더 필요
# TODO:
#   - Review, Practice more
class Solution1:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        l, r, cdict = 0, 0, dict()
        maxlen = 0
        # 1. "r" 이 encounter 하는 character 값 + 1
        # 2. 중복글자 만나면 l 에서부터 shrink window size, current character value 가 1이 될 때 까지
        while r < len(s):
            char = s[r]
            if cdict.get(char, 0) > 0:
                while cdict[char] > 0:
                    cdict[s[l]] -= 1
                    l += 1
            cdict[char] = cdict.get(char, 0) + 1
            maxlen = max(maxlen, r-l+1)
            r += 1
        return maxlen