# 685. Redundant Connection II
'''
In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3
Example 2:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
'''
class Solution:
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        candidate=[]
        self.par=[0]*(len(edges)+1)
        for u,v in edges:
            if self.par[v]!=0:
                candidate.append([self.par[v],v])
                candidate.append([u,v])
            else:
                self.par[v]=u
        if candidate!=[]:
            b1 = self.findCycle(candidate[0][1])
            return candidate[0] if b1 else candidate[1]
        else:
            cycles=self.dfs(edges[0][0])
            for i in reversed(range(len(edges))):
                if tuple(edges[i]) in cycles:
                    return edges[i]
    
    
    def findCycle(self,node):
        seen={}
        while node!=0:
            if node in seen:
                return True
            seen[node]=1
            node=self.par[node]
        return False
    
    def dfs(self,v):
        seen={}
        while v not in seen:
            seen[v]=1
            v=self.par[v]
        edges={}
        u1,v1=self.par[v],v   
        while (u1,v1) not in edges:
            edges[(u1,v1)]=1
            u1,v1=self.par[u1],u1
        return edges
