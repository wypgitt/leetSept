# 387. First Unique Character in a String

'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''
import string
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        uniset = []
        
        for c in string.ascii_lowercase:
            if s.count(c) == 1:
                uniset.append(s.find(c))
        return min(uniset) if len(uniset) > 0 else -1
