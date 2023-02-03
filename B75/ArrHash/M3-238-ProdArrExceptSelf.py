# Solution 1 - Left, Right, Result Array
# Comment: 
#   - 뭔가 부족한것 같은데 뭐가 부족한지를 모르겠다. 복습이 필수일 듯
#   - 이런 유형이 어떤 문제에 대입되는지 알아봐야할 듯
# TODO:
#   - 복습, 정확한 유형 파악
class Solution1:
    # Time: 03' 17"
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        left, right = [0 for _ in range(len(nums))], [0 for _ in range(len(nums))]
        left[0], right[-1] = 1, 1
        res = [0 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        for i in range(len(nums)):
            res[i] = left[i] * right[i]
        return res

    # Time: 02' 00"
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        left, res = [0 for _ in range(len(nums))], [0 for _ in range(len(nums))]
        left[0], res[-1] = 1, 1
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            res[i] = res[i+1] * nums[i+1]
        return [left[i] * res[i] for i in range(len(nums))]

    # Time: 01' 04"
    def productExceptSelf3(self, nums: List[int]) -> List[int]:
        res, R = [0 for _ in range(len(nums))], nums[-1]
        res[0] = 1
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            res[i] = res[i+1] * R
            R *= nums[i]
        return res