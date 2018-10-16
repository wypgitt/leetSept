# 301. Remove Invalid Parentheses

'''
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
'''


class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        level = {s}
        
        while True:
            valids = set(filter(self.isValid, level))
            if len(valids) > 0:
                return list(valids)
            level = {ss[:idx] + ss[idx + 1:] for ss in level for idx in range(len(ss))}

    def isValid(self, s):
        opens = 0
        for pa in s:
            if pa == "(":
                opens += 1
            elif pa == ")":
                if opens == 0:
                    return False
                opens -= 1
        return opens == 0
    
