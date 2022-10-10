class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = len(nums) -  2
        n = len(nums) - 1
        minimum  = [100,100]
        while p >= 0:
            if nums[p] < nums[p+1]: 
                break
            p -= 1
        if p >= 0:
            while n >= 0 and nums[n] <= nums[p]:
                n -= 1
            nums[n],nums[p] = nums[p],nums[n]
            
        r = len(nums) - 1
        p += 1
        while r >= p :
            nums[r],nums[p] = nums[p],nums[r]
            r -= 1
            p += 1