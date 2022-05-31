class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        zero = 0
        for item in nums:
            zero += item
        if zero == 0:
            zero = str(zero)
            return zero
        for i in range (0,len(nums)):
            for j in range(i+1,len(nums)):
                n = int(str(nums[i]) + str(nums[j]))
                m = int(str(nums[j]) + str(nums[i]))
                if m >=n:
                    nums[i],nums[j] = nums[j],nums[i]
        n = ""
        for num in nums:
            n += str(num)
        return n
