
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefixsum = []
        
        sum = 0
        for num in nums:
            sum += num
            prefixsum.append(sum)
        
        ans = []
        print(prefixsum)
        for val in queries:
            
            i = 0
            while i < len(prefixsum) and  prefixsum[i] <= val:
                i += 1
                
            ans.append(i)
        return ans
        