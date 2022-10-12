class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = Counter(arr)
        set = sorted(count)
        ans = 0
        modulo = 10 ** 9 + 7
        for idx1, num in enumerate(set):
            idx2,idx3 = idx1, len(set) - 1
            targeted_sum = target - num
            while idx2 <= idx3:
                second,third = set[idx2],set[idx3]
                
                if second + third < targeted_sum:
                    idx2 += 1
                elif second + third > targeted_sum:
                    idx3 -= 1
                
                else:
                    if idx1 < idx2 < idx3:
                        ans += count[num] * count[second] * count[third]
                    elif idx1 == idx2 < idx3:
                        ans += count[num] * (count[second] - 1)/2 * count[third]
                    elif idx1 < idx2 == idx3:
                        ans += count[num] * (count[second]) * (count[third] - 1)/2
                    else:
                        ans += count[num] *(count[second] - 1)* (count[third] - 2)/6
                    idx2 += 1
                    idx3 -= 1
                    
        return int(ans) % modulo
        
        
        
        
            
            
            
                
        