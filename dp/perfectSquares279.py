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
class Solution:
    _dp = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        import math
        if not n:
            return 0
        
        dp = [n]*(n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            if i*i <= n:
                dp[i*i] = 1
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j += 1
                
                
        return dp[n]  
        
        

        '''     
        '''
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
                    print(queue)        
        '''

        dp = [0]
        while len(dp) <= n:
            tmp = [dp[-i*i] for i in range(1, int(len(dp)**0.5+1))]
            dp += min(tmp) + 1,
        return dp[n]                    
                    
                    
