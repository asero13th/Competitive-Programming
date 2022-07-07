class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        p_s_array = [[pos,spe] for pos,spe in zip(position,speed)]
        for pos,spe in sorted(p_s_array)[::-1]:
            stack.append((target - pos)/spe)
            if len(stack) >= 2and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)