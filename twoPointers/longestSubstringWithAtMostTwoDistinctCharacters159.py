# 159. Longest Substring with At Most Two Distinct Characters
'''
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
'''
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        ans, start, seen = 0, 0, collections.defaultdict(int)
        
        for i, ch in enumerate(s):
            seen[ch] += 1
            if len(seen) <= 2:
                ans = max(ans, i - start + 1)
            while len(seen) > 2:
                seen[s[start]] -= 1
                if seen[s[start]] == 0:
                    seen.pop(s[start])
                start += 1
        return ans
