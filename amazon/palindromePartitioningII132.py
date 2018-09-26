# 132. Palindrome Partitioning II
'''

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return 0
        n = len(s)
        for i in range(1, n):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        dp = [float('inf')]*(n + 1)
        dp[0] = -1
        
        for i in range(n):
            j = 0
            while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                dp[i + j + 1] = min(dp[i + j + 1], dp[i - j] + 1)
                j += 1
            j = 0
            while i - j >= 0 and i + j + 1 < n and s[i - j] == s[i + j + 1]:
                dp[i + j + 2] = min(dp[i + j + 2], dp[i - j] + 1)
                j += 1
        return dp[-1]
