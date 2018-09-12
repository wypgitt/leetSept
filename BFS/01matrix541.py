# 542. 01 Matrix
'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1: 
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2: 
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
'''

class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        que = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = 0x7fffffff
                else:
                    que.append((i, j))
        for i, j in que:
            for r, c in ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)):
                z = matrix[i][j] + 1
                if 0 <= r < m and 0 <= c < n and matrix[r][c] > z:
                    matrix[r][c] = z
                    que.append((r, c))
        return matrix
        

        