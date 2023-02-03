# Solution 1 - Naive Dict, Stack Solution
# Date: 02/02/23
# Time: 02' 57"
# Comment:
#   - Edge Case 좀 더 한번에 잘 생각하기
class Solution1:
    def isValid1(self, s: str) -> bool:
        match = {")":"(", "]":"[", "}":"{"}
        stack = []
        for p in s:
            if p in match:
                if not stack or stack.pop() != match[p]:
                    return False
            else:
                stack.append(p)
        return True if not len(stack) else False