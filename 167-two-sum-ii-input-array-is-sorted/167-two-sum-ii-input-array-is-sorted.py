class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r,l = len(numbers) - 1,0
        while r > l:
            if numbers[r] + numbers[l] == target:
                return sorted([r + 1,l + 1])
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        