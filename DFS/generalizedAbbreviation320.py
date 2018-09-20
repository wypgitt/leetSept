# 320. Generalized Abbreviation
'''
Write a function to generate the generalized abbreviations of a word. 

Note: The order of the output does not matter.

Example:

Input: "word"
Output:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
'''
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
    
        def helper(word, pos, cur, count, result):
            if len(word) == pos:
                result.append(cur + str(count) if count > 0 else cur)
            else:
                helper(word, pos + 1, cur, count + 1, result)
                helper(word, pos + 1, cur + (str(count) if count > 0 else '') + word[pos], 0, result)
            
        result = []
        helper(word, 0, '', 0, result)
        return result
        
        
        
        

