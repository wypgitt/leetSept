# 115. Distinct Subsequences
'''
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
'''
class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        dp = [[0]*(m + 1) for _ in range(n + 1)]
        
        for i in range(m + 1):
            dp[0][i] = 1
        for j in range(1, m + 1):
            for i in range(1, n + 1):
                if s[j - 1] == t[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]
    
        '''
        l1, l2 = len(s)+1, len(t)+1
        cur = [0] * l2
        cur[0] = 1
        for i in range(1, l1):
            pre = cur[:]
            for j in range(1, l2):
                cur[j] = pre[j] + pre[j-1]*(s[i-1] == t[j-1])
        return cur[-1]        

    
        chars, index, dp = set(t), collections.defaultdict(list), [0] * len(t)
        for i, c in enumerate(t): 
            index[c].append(i)
        for c in s:
            if c in chars:
                for i in index[c][::-1]: 
                    dp[i] += dp[i - 1] if i > 0 else 1
        return dp[-1]
        '''
