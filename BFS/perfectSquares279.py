# 279. Perfect Squares

'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''
import collections
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        queue = collections.deque([(0, 0)])
        
        seen = set()
        
        while queue:
            prev, num = queue.popleft()
            num += 1
            for i in range(1, n + 1):
                new = prev + i*i
                if new == n:
                    return num
                if new > n:
                    break
                if new not in seen:
                    seen.add(new)
                    queue.append((new, num))
                    