class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []

        for i,temp in enumerate(temperatures):
            while stack and temperatures[i] > stack[-1][0]:
                ans[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([temp,i])
        return ans