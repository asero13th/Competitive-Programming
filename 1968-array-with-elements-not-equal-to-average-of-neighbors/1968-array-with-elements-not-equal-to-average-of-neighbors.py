class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        average = []
        left = 0
        right = len(nums) - 1
        while len(average) != len(nums):
            average.append(nums[left])
            left += 1

            if right >= left:
                average.append(nums[right])
                right -= 1

        return (average)