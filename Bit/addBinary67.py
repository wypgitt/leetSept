# 67. Add Binary
'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        '''
        a = int(a, 2)
        b = int(b, 2)
        sum_int = a + b
        return bin(sum_int)[2:]




        if len(a) == 0:
            return b
        elif len(b) == 0:
            return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'
        
        
        '''
        a, b = list(a), list(b)
        ans, carry = [], 0
        
        while a or b:
            n1, n2 = 0, 0
            if a:
                n1 = int(a.pop())
            if b:
                n2 = int(b.pop())
            tmp = n1 + n2 + carry
            carry = 0
            if tmp == 1 or tmp == 0:
                ans.append(tmp)
            elif tmp == 2:
                ans.append(0)
                carry += 1
            else:
                ans.append(1)
                carry += 1
        if carry:
            ans.append(carry)
        
        return ''.join(str(s) for s in ans)[::-1]

        
        
        

