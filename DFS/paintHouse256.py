# 256 Paint House

'''
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
             Minimum cost: 2 + 5 + 3 = 10.
'''

class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        #costs = [[17,2,17],[16,16,5],[14,3,19]]
        size = len(costs)
        
        if size == 0:
            return 0
        
        pre = costs[0][:]
        now = [0]*3

        for i in range(size - 1):
            now[0] = min(pre[1], pre[2]) + costs[i + 1][0]
            now[1] = min(pre[0], pre[2]) + costs[i + 1][1]
            now[2] = min(pre[0], pre[1]) + costs[i + 1][2]
            pre[:] = now[:]
            
        return min(pre)
         
'''
class Solution(object):
    def minCost(self, costs):
        r,b,g = 0,0,0
        for rc, bc, gc in costs:
            r,b,g = rc+min(b,g),bc+min(r,g),gc+min(r,b)
        return min([r,b,g])
'''