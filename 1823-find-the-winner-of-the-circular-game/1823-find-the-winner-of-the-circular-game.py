class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [i for i in range(1,n+1)]
        i = 0
        while len(circle) > 1:
            i = (i+(k - 1))%len(circle)
            circle.remove(circle[i])
            print(circle)
        return circle[0]
        