class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #[0,0,1,0,0,0,1,1]
        counter = 0
        hashmap = {0:-1}
        window = 0
        for i, v in enumerate(nums):
            counter += 1 if v else -1
            
            if counter in  hashmap : window = max(window, i - hashmap[counter])
            else:  hashmap[counter] = i
            
        return window
            