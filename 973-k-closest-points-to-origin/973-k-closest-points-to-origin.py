class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for idx,List in enumerate(points):
            d = abs((List[0]**2) + (List[1]**2))
            arr.append([d,idx])
        arr.sort()
        returned_arr = [points[arr[i][1]] for i in range(k)]
        return returned_arr

        
       