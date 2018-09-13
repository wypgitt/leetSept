# 3. Longest Substring Without Repeating Characters

'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        maxL = 0
        dic = {}
        start = 0
        for i, c in enumerate(s):
            if c in dic and start <= dic[c]:
                start = dic[c] + 1
            else:
                maxL = max(maxL, i - start + 1)
            dic[c] = i
        return maxL
        
        
