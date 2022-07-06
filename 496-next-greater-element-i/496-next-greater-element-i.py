class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        stack =[nums2[0]]
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i] and stack[-1] in nums1:
                ans[nums1.index(stack.pop())] = nums2[i]
            if nums2[i] in nums1:
                stack.append(nums2[i])
        return ans
        