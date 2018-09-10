# 490 The Maze

'''
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Example 1

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false
Explanation: There is no way for the ball to stop at the destination.

Note:
There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
'''
import collections
class Solution:
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        m, n = len(maze), len(maze[0])
        
        direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        q = collections.deque()
        q.append((start[0], start[1], None))
        visited[start[0]][start[1]] = True
        
        while q:
            i, j, prev_dir = q.popleft()
            for x, y in direct:
                if (-x, -y) != prev_dir:
                    r, c = i, j
                    while 0 <= r < m and 0 <= c < n and maze[r][c] == 0:
                        r += x
                        c += y
                    r -= x
                    c -= y
                    
                    if [r, c] == destination:
                        return True
                    if visited[r][c]:
                        continue
                    q.append((r, c, (x, y)))
                    visited[r][c] = True
        return False
        
        