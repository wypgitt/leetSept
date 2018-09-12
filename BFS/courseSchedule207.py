# 207. Course Schedule
'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
'''
import collections
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        queue = collections.deque()
        
        take = collections.defaultdict(set)
        require = collections.defaultdict(set)
        
        order = []
        
        for course, pre in prerequisites:
            take[pre].add(course)
            require[course].add(pre)
        for i in range(numCourses):
            if i not in require:
                queue.append(i)
                order.append(i)
        
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                for c in take[cur]:
                    require[c].remove(cur)
                    if not require[c] and c not in order:
                        queue.append(c)
                        order.append(c)
        return len(order) == numCourses
                        
        