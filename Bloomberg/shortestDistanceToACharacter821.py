#821. Shortest Distance to a Character

'''
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
'''
import collections
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        dic = collections.defaultdict(list)
        
        for i, s in enumerate(S):
            dic[s].append(i)
        size = len(S)
        
        return [min([abs(i - c) for c in dic[C]]) for i in range(size)]
