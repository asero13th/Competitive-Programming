class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        tmp = ["".join(sorted(str)) for str in strs]
        hashmap ={}
        for idx,str in enumerate(tmp):
            if not str in hashmap: hashmap[str] = [idx]
            else: hashmap[str].append(idx)
        for strarr in hashmap:
            c = 0
            tmp = []
            while c < len(hashmap[strarr]):
                tmp.append(strs[hashmap[strarr][c]])
                c += 1
            ans.append(tmp)
        return ans
        
        