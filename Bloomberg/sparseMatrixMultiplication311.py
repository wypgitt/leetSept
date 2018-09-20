# 311. Sparse Matrix Multiplication
'''
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |

'''
class Solution:
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
	'''
        if A is None or B is None:
            return None
        m, n, l = len(A), len(A[0]), len(B[0])
        ans = [[0]*l for _ in range(m)]
        if len(B) != n:
            raise Exception
        for i, row in enumerate(A):
            for j, eA in enumerate(row):
                if eA:
                    for k, eB in enumerate(B[j]):
                        if eB:
                            ans[i][k] += eA*eB
        return ans
        '''
        m, n, l = len(A), len(A[0]), len(B[0])
        if n != len(B):
            return []
        tableB = {}
        for k in range(len(B)):
            tableB[k] = {}
            for j in range(len(B[0])):
                if B[k][j]:
                    tableB[k][j] = B[k][j]
        ans = [[0]*l for _ in range(m)]
        for i in range(len(A)):
            for k in range(len(A[0])):
                if A[i][k]:
                    for j, value in tableB[k].items():
                        ans[i][j] += value*A[i][k]
        return ans



