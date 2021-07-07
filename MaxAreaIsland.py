#  Max Area of Island

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        no_rows=grid.length
        no_cols=grid[0].length
        for row_no,rows in enumerate(grid):
            for col_no,cell in enumerate(rows):
                if cell==1:
                    maxAreaOfIsland(self,List[List[int]])
                    print(row_no,col_no,cell)