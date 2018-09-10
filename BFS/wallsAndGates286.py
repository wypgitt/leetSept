# 286. Walls and Gates

'''
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

'''

class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """

        if not rooms:
            return
        
        que = [(i, j) for i, row in enumerate(rooms) for j, r in enumerate(row) if not r]
        
        for x, y in que:
            for i, j in (x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1):
                if 0 <= i < len(rooms) and 0 <= j < len(rooms[0]) and rooms[i][j] > 2**30:
                    rooms[i][j] = rooms[x][y] + 1
                    que.append((i, j))