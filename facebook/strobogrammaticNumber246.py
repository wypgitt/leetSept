# 246. Strobogrammatic Number
'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false
'''
class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        #return all(num[i] + num[~i] in '696 00 11 88' for i in range(len(num)//2+1))
        
        maps = {("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}
        i, j = 0, len(num) - 1
        while i <= j:
            if (num[i], num[j]) not in maps:
                return False
            i += 1
            j -= 1
        return True
    
