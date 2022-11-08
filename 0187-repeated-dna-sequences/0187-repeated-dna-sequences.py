class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashmap = {}
        str = []
        ans = []
        if len(s) <= 10:
            return []
        
        for i in range(10):
            str += s[i]
            
        val = ''.join(str)
        hashmap[val] = 1
        
        for i in range(10,len(s)):
            str.append(s[i])
            str.remove(str[0])
            
            val = ''.join(str)
            hashmap[val] = 1 + hashmap.get(val, 0)
            
            if hashmap[val] == 2:
                ans.append(val)
        return ans
            
            
           
        
        