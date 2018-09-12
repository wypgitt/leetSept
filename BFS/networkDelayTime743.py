# 743. Network Delay Time
'''
DescriptionHintsSubmissionsDiscussSolution
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Note:
N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.
'''
import collections
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        nodes = collections.defaultdict(dict)
        
        for u, v, w in times:
            nodes[u - 1][v - 1] = w
        Q =set(range(N))
        
        dist = N*[float('inf')]
        
        dist[K - 1] = 0
        
        while Q:
            n = None
            for node in Q:
                if n == None or dist[node] < dist[n]:
                    n = node
            Q.remove(n)
            
            for v in nodes[n]:
                alt = dist[n] + nodes[n][v]
                if alt < dist[v]:
                    dist[v] = alt
        return max(dist) if max(dist) != float('inf') else - 1
        

        
