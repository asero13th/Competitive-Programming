class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        mn = 1
        sum = 0
        for num in nums:
            sum += num
            
            if sum < 0:
                mn = max(abs(sum) + 1,mn)
        return mn