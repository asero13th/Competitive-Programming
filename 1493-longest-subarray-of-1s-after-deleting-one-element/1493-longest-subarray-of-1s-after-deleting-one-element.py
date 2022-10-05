class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        right, left = 0,0
        zero = 1
        result = 0

        while right<len(nums):
            
            while nums[right] == 0 and zero == 0:
                if nums[left] == 0:
                    zero += 1    
                left += 1
                
            if nums[right] == 0 and zero == 1:
                zero -= 1

            result  = max(result,right - left)   
            right += 1
            
        return result
             
            
        