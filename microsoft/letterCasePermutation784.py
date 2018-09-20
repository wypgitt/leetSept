# 784. Letter Case Permutation
'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length at most 12.
S will consist only of letters or digits.\
'''
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        
        '''
        ans = [[]]
        
        for ch in S:
            n = len(ans)
            if ch.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(ch.lower())
                    ans[n + i].append(ch.upper())
            else:
                for i in range(n):
                    ans[i].append(ch)
        return map("".join, ans)
        '''


        f = lambda x: (x.lower(), x.upper()) if x.isalpha() else x
        return map("".join, itertools.product(*map(f, S)))
        

