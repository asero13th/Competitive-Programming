class Solution:
    def countVowels(self, word: str) -> int:
        l = len(word)
        c = 0
        
        for i in range(l):
            if word[i] in "aeiou":
                c += (i + 1) * (l - i)
        return c
        
        
        