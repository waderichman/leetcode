class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        curr = image[sr][sc]
        self.dfs(image, sr, sc, newColor, curr)
        return image
        
    def dfs(self, image, sr, sc, newColor, curr):
        if sr < 0 or sr > len(image)-1 or sc < 0 or sc > len(image[0])-1 or image[sr][sc] == newColor or image[sr][sc] is not curr:
            return 0
            
        image[sr][sc] = newColor
        self.dfs(image, sr+1, sc, newColor, curr)
        self.dfs(image, sr-1, sc, newColor, curr)
        self.dfs(image, sr, sc+1, newColor, curr)
        self.dfs(image, sr, sc-1, newColor, curr)
        