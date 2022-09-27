class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        arr = s.split()
        num = -1
        for i in arr:
            if i.isdigit():
                if int(i) > num:
                    num = int(i)
                else:
                    return False
        return True
        