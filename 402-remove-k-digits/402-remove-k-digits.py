class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and len(stack) != 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
            
        stack = stack[:len(stack) - k]
        result = "".join(stack)
        if stack:
            return str(int(result))
        else:
            return "0"
        