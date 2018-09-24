# 64. Minimum Path Sum
'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')]*n for _ in range(m)]
        pi = [[0]*n for _ in range(m)]
        if not grid:
            return 0
        for i in range(m):
            for j in range(n):
                tmp = float('inf')
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                    continue
                if i > 0:
                    tmp= min(tmp, dp[i - 1][j])
                    if tmp == dp[i - 1][j]:
                        pi[i][j] = 1
                    
                if j > 0:
                    tmp = min(tmp, dp[i][j - 1])
                    if tmp == dp[i][j - 1]:
                        pi[i][j] = 0
                
                dp[i][j] = tmp + grid[i][j]
                
        path = [0]*(m + n - 1)
        x, y = m - 1, n - 1
        for p in range(m + n - 1):
            path[p] = grid[x][y]
            if pi[x][y] == 0:
                x -= 1
            else:
                y -= 1
        
        for p in range(m + n - 2, -1, -1):
            print(path[p])
        
        return dp[m - 1][n - 1]        
        '''
        '''
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')]*n for _ in range(m)]
        if not grid:
            return 0
        for i in range(m):
            for j in range(n):
                tmp = float('inf')
                if i == 0 and j == 0:
                    dp[i%2][j] = grid[i][j]
                    continue
                if i > 0:
                    tmp= min(tmp, dp[1 - i%2][j])
                if j > 0:
                    tmp = min(tmp, dp[i%2][j - 1])
                
                dp[i%2][j] = tmp + grid[i][j]
        return dp[(m - 1)%2][n - 1]          
        '''
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')]*n for _ in range(2)]
        if not grid:
            return 0
        old, new = 0, 0
        for i in range(m):
            old = new
            new = 1 - new
            for j in range(n):
                tmp = float('inf')
                if i == 0 and j == 0:
                    dp[new][j] = grid[i][j]
                    continue
                if i > 0:
                    tmp= min(tmp, dp[old][j])
                if j > 0:
                    tmp = min(tmp, dp[new][j - 1])
                
                dp[new][j] = tmp + grid[i][j]
        return dp[new][n - 1]  
  
