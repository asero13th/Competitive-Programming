class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = [0] * (len(nums))
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            s[i] = sum
        if s[-1] - s[0] == 0:
            return 0
        for i in range(1,len(nums)):
            if s[i - 1] == s[-1] - s[i]:
                return i
        if s[-1] - s[len(s) -2] == s[-1]:
            return len(s) - 1
        return -1
        