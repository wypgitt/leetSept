# 265. Paint House II
'''

There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5. 
Follow up:
Could you solve it in O(nk) runtime?
'''
class Solution:
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or len(costs[0]) == 0:
            return 0
        n, k = len(costs), len(costs[0])
        for i in range(1, n):
            min1 = min(costs[i - 1])
            idx = costs[i - 1].index(min1)
            
            min2 = min(costs[i - 1][:idx] + costs[i - 1][idx+ 1:])
            for j in range(k):
                if j == idx:
                    costs[i][j] += min2
                else:
                    costs[i][j] += min1
        return min(costs[len(costs) - 1])


        
        

        '''
        if costs is None or len(costs) == 0:
            return 0  
        # 初始化
        k = len(costs[0])
        old_cost = [0 for _ in range(k)]
        new_cost = [0 for _ in range(k)]
        
        for cost in costs:
            for i in range(k):
                # 当前 上一个房子非i颜色的最小cost + 当前的颜色i的cost  
                new_cost[i] = min(old_cost[:i] + old_cost[i+1:]) + cost[i]
            # 更新cost    
            old_cost[:] = new_cost[:]
        
        return min(new_cost) 
        '''
        '''
        if not costs or len(costs) == 0:
            return 0
        n, k = len(costs), len(costs[0])
        dp = [[0]*k for _ in range(n + 1)]
        
        for i in range(k):
            dp[0][i] = 0
        id1, id2 = 0, 0
        for i in range(1, n + 1):
            min1, min2 = float('inf'), float('inf')
            for j in range(k):
                if dp[i - 1][j] < min1:
                    min2 = min1
                    min1 = dp[i - 1][j]
                    id2 = id1
                    id1 = j
                else:
                    if dp[i - 1][j] < min2:
                        min2 = dp[i - 1][j]
                        id2 = j
            for j in range(k):
                dp[i][j] = costs[i - 1][j]
                if j != id1:
                    dp[i][j] += min1
                else:
                    dp[i][j] += min2
        ans = float('inf')
        for i in range(k):
            ans = min(ans, dp[n][i])
        return ans
            
        '''


        

