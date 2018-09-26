# 140. Word Break II
'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
'''
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        '''
        # method 1: iterative with 2 for loop (MLE)
        res = []
        dp = [[] for i in range(len(s)+1)]
        dp[0].append('')
        if not s or not wordDict:
            return res
        for i in range(1, len(dp)):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i].extend([(sub and sub + ' ') + s[j:i] for sub in dp[j]])
        return dp[-1]
               
        '''
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, memory):
        if s in memory:
            return memory[s]
        ans = []
        cnt = 0
        for word in wordDict:
            if word == s[:len(word)]:
                next_word = s[len(word):]
                if len(next_word) == 0:
                    ans.append(word)
                    cnt += 1
                else:
                    for w in self.dfs(next_word, wordDict, memory):
                        cnt += 1
                        ans.append(word + ' ' + w)
        memory[s] = ans
        print(cnt)
        return ans

