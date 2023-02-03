# Solution 1 - Using Complement & Dictionary
# Comment:
#   - Various solutions exist, since it's a core problem, should dig in more
# TODO:
#   - Look for better solutions
class Solution1:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        ndict = dict()  # key = number, value = index
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in ndict.keys():
                return [ndict[comp], i]
            ndict[nums[i]] = i
        return [-1, -1]