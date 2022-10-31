class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        for n in c:
            if c[n] > len(nums)//2:
                return n