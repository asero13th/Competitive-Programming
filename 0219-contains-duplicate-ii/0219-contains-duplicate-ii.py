class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        c = Counter(nums)
        hashmap = {}
        for i,num in enumerate(nums):
            
            if c[num] > 1:
                if num in hashmap and i - hashmap[num] <= k:
                        return True
                else:
                    hashmap[num] = i
                        
        return False
                 