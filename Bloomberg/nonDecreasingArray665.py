# 665. Non-decreasing Array
'''

Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
'''
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        p = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if p is not None:
                    return False
                p = i
        return p is None or p == 0 or p== len(nums) - 2 or nums[p - 1] <= nums[p + 1] or nums[p] <= nums[p + 2]
        
        '''
        
        if nums == [] or len(nums) == 0:
            return True
        change = False
        
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] > nums[i + 1]:
                if change:
                    return False
                else:
                    if i - 1 < 0 or nums[i - 1] <= nums[i + 1]:
                        nums[i] = nums[i + 1]
                    else:
                        nums[i + 1] = nums[i]
                    
                    change = True
        return True
        
        
        


