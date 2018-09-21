# 360. Sort Transformed Array
'''
Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example 1:

Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
Example 2:

Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
'''
class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        nums = [a*x*x + b*x + c for x in nums]
        
        i, j = 0, len(nums) - 1
        ans = [0]*len(nums)
        curr = 0
        while i <=j:
            if (a > 0)^(nums[i] > nums[j]):
                ans[curr] = nums[j]
                j -= 1
                curr += 1
                
            else:
                ans[curr] = nums[i]
                i += 1
                curr += 1
                
        return ans[::-1] if a > 0 else ans 
