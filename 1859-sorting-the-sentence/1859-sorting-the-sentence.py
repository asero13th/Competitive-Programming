class Solution:
    def sortSentence(self, s: str) -> str:
        n = s.split(" ")
        for i in range(0,len(n)):
             for j in range(i + 1,len(n)):
                     if n[j][len(n[j]) - 1] < n[i][len(n[i]) - 1]:
                            tmp = n[i]
                            n[i] = n[j]
                            n[j] = tmp
        s =  ' '.join(n)
        n = []
        for i in range(0,len(s) - 1):
            if s[i].isdigit():
                 continue
            n.append(s[i])
        s = ''.join(n)
        return s
