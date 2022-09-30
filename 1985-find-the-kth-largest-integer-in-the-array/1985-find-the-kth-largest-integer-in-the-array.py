class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        num = [int(i) for i in nums]
        num.sort()
        n = str(num[len(num) - k])
        return n