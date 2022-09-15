class Solution:
    def findKthBit(self, n: int, k: int) -> str:
            def helper(n: int , k : int):
                if n == 1:
                    return "0"
                else:
                    result = str(helper(n - 1,k))
                    invert = ""
                    for ch in reversed(result):
                        invert += str(1 - int(ch))
                    return result +"1" + invert
            ans = helper(n,k)
            return ans[k - 1]
            