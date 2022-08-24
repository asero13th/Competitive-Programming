class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        decq = []
        incq = []
        length,left  = 0,0
        for idx,num in enumerate(nums):
            while decq and num > decq[-1]:
                decq.pop()
            decq.append(num)
            while incq and num <incq[-1]:
                incq.pop()
            incq.append(num)
            while decq[0] - incq[0] > limit:
                if decq[0] == nums[left]:
                    decq.pop(0)

                if incq[0] == nums[left]:
                    incq.pop(0)
                left += 1
            length = max(length,idx-left + 1)
        return length
        