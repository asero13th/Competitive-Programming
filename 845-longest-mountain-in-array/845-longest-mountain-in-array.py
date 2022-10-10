class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = 0
        for i in range(1,len(arr) - 1):
            
            if arr[i - 1] < arr[i] > arr[ i + 1]:
                l , r = i,i
                
                while l > 0 and arr[l - 1] < arr[l]:
                    l -= 1
                
                while r + 1 < len(arr) and arr[r + 1] < arr[r]:
                    r += 1
                    
                res = max(res,r  - l + 1)
        return res
                    
            
        