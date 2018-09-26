# 131. Palindrome Partitioning
'''

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

'''
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        ans = []
        self.dfs(s, [], ans)
        return ans
    def dfs(self, s, path, ans):
        if not s:
            ans.append(path)
        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], path + [s[:i]], ans)
        
    def isPalindrome(self, s):
        return s == s[::-1]
