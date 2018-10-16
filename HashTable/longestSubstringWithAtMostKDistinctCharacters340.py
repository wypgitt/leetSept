# 340. Longest Substring with At Most K Distinct Characters
'''
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
'''
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or not k:
            return 0
        longest_substring = 0
        slow, fast, n = 0, 0, len(s)
        chaDict = {}
        curr_string = 0
        while fast < n:
            if s[fast] in chaDict:
                chaDict[s[fast]] += 1
            else:
                chaDict[s[fast]] = 1
                curr_string += 1
            if curr_string > k:
                while slow < fast and curr_string > k:
                    chaDict[s[slow]] -= 1
                    if chaDict[s[slow]] == 0:
                        del chaDict[s[slow]]
                        curr_string -= 1
                    slow += 1
            longest_substring = max(longest_substring, fast - slow + 1)
            fast += 1
        return longest_substring
                
        
        
        
        
        
