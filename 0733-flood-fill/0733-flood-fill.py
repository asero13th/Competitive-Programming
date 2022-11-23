class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image == None or image[sr][sc] == color:
            return image
        
        self.fill(image,sr,sc,image[sr][sc],color)
        return image
        
        
    def fill(self,image,r,c,initial,color):
        if r < 0 or r >= len(image): return
        if  c < 0 or c >= len(image[0]):return 
        if image[r][c] != initial: return
        if image[r][c] == color: return
        
        image[r][c] = color
        self.fill(image,r-1,c,initial,color)
        self.fill(image,r+1,c,initial,color)
        self.fill(image,r,c+1,initial,color)
        self.fill(image,r,c-1,initial,color)
            
        
        