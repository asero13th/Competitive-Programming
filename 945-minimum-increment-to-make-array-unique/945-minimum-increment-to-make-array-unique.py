class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        m = 0
        dup = []
        c = Counter(nums)
        for i in range(len(nums) + max(nums)):
            if c[i] > 1:
                dup.extend([i] * (c[i] -1))

            elif not c[i] and dup:
                ld = dup.pop()
                m += i - ld
        return m
        