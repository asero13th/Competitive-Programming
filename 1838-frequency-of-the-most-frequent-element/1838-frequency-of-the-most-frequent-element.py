class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        right,left = 0,0
        answer, total_sum = 0,0

        while right <len(nums):
            total_sum  += nums[right]
            while nums[right] * (right - left + 1) > total_sum + k:
                total_sum -= nums[left]
                left += 1

            answer = max(answer,right - left + 1)
            right += 1
        return answer
        