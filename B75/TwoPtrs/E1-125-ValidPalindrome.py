# Solution 1 - Naive Solution
# Comments:
#   - 에디터를 너무 믿지말 것
# TODO:
#   - Review built in functions
class Solution1:
    def isPalindrome1(self, s: str) -> bool:
        s = "".join(s.split())
        l, r = 0, len(s)-1
        while l < r:
            while l < len(s) and not s[l].isalnum():
                l += 1
            while -1 < r and not s[r].isalnum():
                r -= 1
            if r < l:
                break
            
            if s[l].isalpha() and s[r].isalpha() and s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            elif s[l].isdigit() and s[r].isdigit() and int(s[l]) == int(s[r]):
                l += 1
                r -= 1
            else:
                print(l, s[l])
                print(r, s[r])
                return False
        return True

# Solution 2 - Naive Revisiting
# 02/02/23
class Solution2:
    def isPalindrome1(self, s: str) -> bool:
        s = "".join(s.split())
        l, r = 0, len(s) - 1
        while l < r:
            while l < len(s) and not s[l].isalnum():
                l += 1
            while r > -1 and not s[r].isalnum():
                r -= 1
            if l >= r:
                break
            if s[l].isdigit() and s[r].isdigit() and s[l] == s[r]:
                l += 1
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True