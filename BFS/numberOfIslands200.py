# 200. Number of Islands

'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''
import collections
class Solution(object):
    #dfs
    def numIslands1(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        cnt = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    cnt += 1
        return cnt
        
        
        
    def dfs(self, grid, a, b):
        
        if a < 0 or b < 0 or a >= len(grid) or b >= len(grid[0]) or grid[a][b] != '1':
            return 
        grid[a][b] = '#'
        
        self.dfs(grid, a + 1, b)
        self.dfs(grid, a - 1, b)
        self.dfs(grid, a, b - 1)
        self.dfs(grid, a, b + 1)

#Time complexity : O(M \times N)O(M×N) where MM is the number of rows and NN is the number of columns.

#Space complexity : worst case O(M \times N)O(M×N) in case that the grid map is filled with lands where DFS goes by M \times NM×N deep.


#BFS:

def numIslands2(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """ 
    if not grid:
        return 0
    
    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                self.bfs(grid, i, j)
                islands += 1
    return islands

def bfs(self, grid, x, y):
    queue = collections.deque([(x, y)])
    grid[x][y] = '#'

    while queue:
        x, y = queue.popleft()
        for delta_x, delta_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_x = x + delta_x
            next_y = x + delta_y
            if next_x < 0 or next_y < 0 or next_x >= len(grid) or next_y >= len(grid[0]) or grid[next_x][next_y] != '1':
                continue
            queue.append((next_x, next_y))
            grid[next_x][next_y] = '#'