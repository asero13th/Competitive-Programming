class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for num in c:
            if c[num] != 1: return True
        return False