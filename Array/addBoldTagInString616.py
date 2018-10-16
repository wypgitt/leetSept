# 616. Add Bold Tag in String
'''
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:
Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Example 2:
Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
'''
class Solution:
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        status = [False]*len(s)
        added = ""
        for word in dict:
            start = s.find(word)
            end = len(word)
            while start != -1:
                for i in range(start, end + start):
                    status[i] = True
                start = s.find(word, start + 1)
        i = 0
        print(status)
        while i < len(s):
            if status[i]:
                added += '<b>'
                while i < len(s) and status[i]:
                    added += s[i]
                    i += 1
                added += '</b>'
            else:
                added += s[i]
                i += 1
        return added

    
    
    
    
    
    
    #[True, False, False, True, False, True, False]
