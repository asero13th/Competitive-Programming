class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num_counter = [0]
        m = len(nums) - 1
        for i in range(0,m):
            num_counter.append(0)
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[j] < nums[i]:
                     num_counter[i] += 1
        return num_counter 
 