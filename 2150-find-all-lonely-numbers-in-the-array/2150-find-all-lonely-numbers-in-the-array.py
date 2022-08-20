class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        nums.sort()
        lonely_num = []
        for i in range(len(nums)):
            if len(nums) == 1:
                lonely_num.append(nums[0])
                return lonely_num
            if i - 1 < 0:
                if nums[i] + 1 < nums[i + 1]:
                    lonely_num.append(nums[i])
            elif i + 1 == len(nums):
                if nums[i] - 1 > nums[i - 1]:
                    lonely_num.append(nums[i])
            elif nums[i] + 1 < nums[i+1] and nums[i] - 1 > nums[i - 1]:
                    lonely_num.append(nums[i])
        return lonely_num
        