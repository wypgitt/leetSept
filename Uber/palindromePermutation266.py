# 266. Palindrome Permutation

'''
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
'''
import collections
class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        dic = collections.Counter(s)
        
        odd = 0
        for cnt in dic.values():
            if cnt%2 == 1:
                odd += 1
                
        if odd > 1:
            return False
        return True
       
            
        