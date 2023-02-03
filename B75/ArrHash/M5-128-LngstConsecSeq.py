# Solution 1: Using Hash Set
# Comments:
#   - 뭔가 머리속에서 루프 돌리는걸 잘 못한다, 타개할 방법을 찾는게 중요하다
# TODO:
#   - Need to practice on building a solid algorithm from the start
class Solution:
    # Time: 05' 09"
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxcnt = float('-inf')
        for num in nums:
            if num-1 not in numset:
                curnum, curcnt = num, 1
                while curnum+1 in numset:
                    curnum += 1
                    curcnt += 1
                maxcnt = max(maxcnt, curcnt)
        return maxcnt
            