# Solution 1 - Use Hash Set
# Comments: 
#   - Look for other better possible solutions
# TODO: None
class Solution1:
    def containsDuplicate1(self, nums: List[int]) -> bool:
        numset = set(nums)
        return len(numset) < len(nums)

    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)