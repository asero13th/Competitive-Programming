class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum = len(nums)
        l = 0
        sum  = 0
        check = 0
        for r,val in enumerate(nums):
            sum += val
            c = 0
            while sum >= target and r >= l:
                sum -= nums[l]
                minimum = min(minimum,r - l + 1)
                l += 1
                check = 1
        return minimum if check else 0
            
            