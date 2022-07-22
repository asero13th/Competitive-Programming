class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted([[i,v] for v,i in enumerate(nums)])
        r,l = len(nums) - 1,0
        while r > l:
            if sorted_nums[r][0] + sorted_nums[l][0] == target:
                return [sorted_nums[r][1],sorted_nums[l][1]]
            elif sorted_nums[r][0] + sorted_nums[l][0] > target:
                if sorted_nums[r][0] > sorted_nums[l][0]:
                    r -= 1
                else:
                    l += 1
            else:
                if sorted_nums[r][0] > sorted_nums[l][0]:
                    l += 1
                else:
                    r -= 1
        return []
        