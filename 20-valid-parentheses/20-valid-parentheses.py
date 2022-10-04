class Solution:
    def isValid(self, s: str) -> bool:
            stack = []
            bmap = {
                
                '(':')',
                '{':'}',
                '[':']'
            }
            
            for i in s:
                if i in bmap.keys():
                    stack.append(i)
                else:
                    if stack and i == bmap[stack[-1]]:
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0
                
