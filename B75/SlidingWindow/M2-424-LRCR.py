# Solution 1: Naive 26-len array approach
# Date: 02/02/23
# Time: 10' 41"
# Comment:
#   - 머릿속 시뮬레이션 잘 안되니까 노트로 돌리는법 연습
#   - 좀 확실하게 시뮬 잘 돌리는법 없는지, 시뮬 연습 더하기
# TODO:
#   - 시뮬레이션 연습
class Solution1:
    def characterReplacement1(self, s: str, k: int) -> int:
        # If curlen - maxcount > k => Shrink the window size + Edit the char array
        # ord(char) - 65
        alphas = [0] * 26
        l, r = 0, 0
        res = 0
        while r < len(s) and l < len(s):
            alphas[ord(s[r]) - 65] += 1
            while (r-l+1) - max(alphas) > k and l < len(s):
                alphas[ord(s[l])-65] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res