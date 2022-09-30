class Solution:
    def smallestNumber(self, num: int) -> int:
        arr = []
        str1 = str(num)
        arr = [i for i in str1 if i.isdigit()]
        arr.sort()
        
        if str1[0] == "-":
            arr.reverse()
            return int("-"+"".join(arr))
        else:
            c = 0
            for i in range(len(arr)):
                if arr[i] =='0':
                    c += 1
                elif arr[i] != '0' and c != 0:
                    arr[i],arr[0] = arr[0],arr[i]
                    break
            return int("".join(arr))
                    
            
                    
                    
                