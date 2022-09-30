class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        num = [int(i) for i in nums]
        num.sort()
        return str(num[len(num) - k])