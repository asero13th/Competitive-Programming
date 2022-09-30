class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        other_num = []
        for item in nums:
            other_num.append(int(item))
        other_num.sort()
        num = other_num[::-1]
        return (str(num[k - 1]))