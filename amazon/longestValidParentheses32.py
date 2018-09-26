# 32. Longest Valid Parentheses
'''

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n, left, right, maxans = len(s), 0, 0, 0
        for i in range(n):
            if s[i] == '(':
                left += 1
            elif s[i] == ')':
                right += 1
            if left == right:
                maxans = max(maxans, 2*left)
            elif right >= left:
                left = right = 0
                
        left = right = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '(':
                left += 1
            elif s[i] == ')':
                right += 1
            if left == right:
                maxans = max(maxans, 2*right)
            elif left >= right:
                left = right = 0
        
        return maxans

        '''
        maxans, n = 0, len(s)
        dp = [0]*(n)
        for i in range(n):
            if s[i] == ')':
                if i - 1 >= 0 and s[i - 1] == '(':
                    if i - 2 >= 0:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    if i - dp[i - 1] >= 2:
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2                        
                    else:                    
                        dp[i] = dp[i - 1] + 2
            maxans = max(maxans, dp[i])
        return maxans        
        '''
