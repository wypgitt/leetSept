# 243. Shortest Word Distance

'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

'''
import collections
class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        hashmap = collections.defaultdict(list)
        for i, word in enumerate(words):
            hashmap[word].append(i)
        
        ans = float('inf')
        for p1 in hashmap[word1]:
            for p2 in hashmap[word2]:
                ans = min(ans, abs(p1 - p2))
        return ans