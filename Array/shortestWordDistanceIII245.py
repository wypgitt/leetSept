# 245. Shortest Word Distance III
'''

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “makes”, word2 = “coding”
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3
Note:
You may assume word1 and word2 are both in the list.
'''
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """

        n = len(words)
        ans = n
        p1 = p2 = -n
        same = word1 == word2
        
        for i in range(n):
            if words[i] == word1:
                p1 = i
                ans = min(ans, i - p2)
                if same:
                    p2 = p1
            elif not same and words[i] == word2:
                p2 = i
                ans = min(ans, i - p1)
        return ans
        
        
        

                
