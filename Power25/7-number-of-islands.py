class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numOfIslands = 0
        if grid is None or len(grid) == 0:
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    numOfIslands += self.exploreIslands(grid,i,j)
        return numOfIslands
    
    def exploreIslands(self,grid,i,j):
        
        if self.invalidCoordinate(grid,i,j):
            return 0
        
        grid[i][j] = '0'
        self.exploreIslands(grid, i-1, j)
        self.exploreIslands(grid, i+1, j)
        self.exploreIslands(grid, i, j+1)
        self.exploreIslands(grid, i, j-1)

        return 1
    
    def invalidCoordinate(self,grid,i,j):
        return (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0')
        
