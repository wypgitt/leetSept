# 679. 24 Game


'''
You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False
Note:
The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
'''
class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        
        
        
        
        

        '''
        if len(nums) == 1:
            return abs(nums[0] - 24) <= 0.001
        for i in range(len(nums)):
            for j in range(0, i):
                a = nums[i]
                b = nums[j]
                nxt = [a + b, a - b, b - a, a*b]
                if abs(a) > 0.001:
                    nxt.append(float(b)/float(a))
                if abs(b) > 0.001:
                    nxt.append(float(a)/float(b))
                nums.pop(i)
                nums.pop(j)
                for n in nxt:
                    nums.append(n)
                    if self.judgePoint24(nums):
                        return True
                    nums.pop()
                nums.insert(j, b)
                nums.insert(i, a)
        return False
        '''
        
        
