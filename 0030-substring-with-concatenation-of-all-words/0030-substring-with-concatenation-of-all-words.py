class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or s is None:
            return []
        count = {}
        wordlength = len(words[0])
        res = []
        wordslength = len(words) * wordlength
        
        for word in words:
            count[word] = count.get(word,0) + 1
        
        for left in range(len(s) - wordslength + 1):
            wordseen = {}
            
            for right in range(len(words)):
                wordindex = left+right * wordlength
                
                tempword = s[wordindex: wordindex + wordlength]
                
                if tempword not in count:
                    break
                
                wordseen[tempword] = wordseen.get(tempword,0) + 1
                
                if wordseen[tempword] > count[tempword]:
                    break
            if wordseen == count:
                res.append(left)
        return res
                
                
                
#         hashmap = {}
#         ans = []
#         length = len(words[0])*len(words)
#         w = len(words[0])
#         l = len(words)
        
#         dictionary = {}
#         for word in words:
#             hashmap[word] = hashmap.get(word,0) + 1
        
#         for i in range(0,w*l,w):
#             str = s[i:i+w]
#             dictionary[str] = dictionary.get(str,0) + 1
#         if dictionary == hashmap:
#             ans.append(0)
        
#         for i in range(w,len(s),w):
#             str = s[i:i+w]
#             str2 = s[i-w:i]
#             dictionary[str] = dictionary.get(str,0) + 1
#             dictionary[str2] -= 1
#             checker  = 0
#             for key in dictionary:
#                 if key in hashmap:
#                     if hashmap[key] == dictionary[key]:
#                         checker += 1
#             if checker == len(dictionary):
#                 ans.append(i)
#             print(dictionary)
            
#         return ans
        
            
        
        
        
            
            
            
            
            
        
        
        
        
        