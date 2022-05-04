class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    self.dfs(i,j,grid)
                    count+=1
        return count
    def dfs(self,i,j,grid):
        if grid[i][j]=="1":
            grid[i][j] = "v"
            if i+1<len(grid): self.dfs(i+1,j,grid)
            if i-1>=0: self.dfs(i-1,j,grid)
            if j+1<len(grid[0]) : self.dfs(i,j+1,grid)
            if j-1>=0 : self.dfs(i,j-1,grid)