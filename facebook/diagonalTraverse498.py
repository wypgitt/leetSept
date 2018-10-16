# 498. Diagonal Traverse
'''

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:

Note:
The total number of elements of the given matrix will not exceed 10,000.
'''
class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        x, y = 0, 0
        if not matrix or not matrix[0]:
            return ans
        M, N = len(matrix), len(matrix[0])
        for _ in range(M*N):
            ans.append(matrix[x][y])
            if (x+y)&1:
                if x == M - 1:
                    y += 1
                elif y == 0:
                    x += 1
                else:
                    x += 1
                    y -= 1
            else:
                if y == N - 1:
                    x += 1
                elif x == 0:
                    y += 1
                else:
                    x -= 1
                    y += 1
        return ans
