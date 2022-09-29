class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0,len(nums) - 1
        arr = [-1,-1]
        while l <= r:
            if nums[l] == target and arr[0] == -1:
                arr[0] = l
            if nums[r] == target and arr[1] == -1:
                arr[1] = r
            if arr[0] != -1 and arr[1] != -1:
                break
            if nums[r] != target:
                r -= 1
            if nums[l] != target:
                l += 1
        return arr
            
            