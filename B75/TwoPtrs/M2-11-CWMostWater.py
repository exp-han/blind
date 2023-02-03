# Solution 1 - Two Pointers 정석 Approach
# Comment: 
#   - 더 나은 솔루션 찾아보기 / 다른 접근법
class Solution1:
    def maxArea1(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxera = float('-inf')
        while l < r:
            maxera = max(maxera, (r-l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxera