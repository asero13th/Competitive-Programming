class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]: 
            answer = []
            for i in range(len(l)):
                sorted_list = [nums[j] for j in range(l[i],r[i] + 1)]
                sorted_list.sort()
                new_list = [(sorted_list[k] - sorted_list[k - 1]) for k in          range(1,len(sorted_list))]
                if len(Counter(new_list)) == 1:
                    answer.append(True)
                else:
                    answer.append(False)
            return answer
        
        