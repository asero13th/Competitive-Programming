class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        arr = [i for i in range(len(nums)) if nums[i] == target]
        return arr
        