class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operation = 0
        c = Counter(nums)
        _set = set()
        
        for item in c:
            if item not in _set and (k - item) in c :
                if item == (k - item):
                    operation += c[item]//2
                else:
                    operation += min(c[item], c[k-item])
                _set.add(item)
                _set.add(k - item)
                
        return operation
        