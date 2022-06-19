class Solution:
    def isValid(self, s: str) -> bool:
            symbol_match = {
                '}':'{',
                ']':'[',
                ')':'('
            }
            stack = []
            s = list(s)
            for i in range(len(s)):
                if s[i] in symbol_match.keys():
                    if not stack:
                        return False
                    if symbol_match[s[i]] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(s[i])
            return len(stack) == 0