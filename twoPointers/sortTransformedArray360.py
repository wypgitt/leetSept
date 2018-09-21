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
        ans = [0]*len(nums)
        p1, p2 = 0, len(nums) - 1
        i, d = (p1, 1) if a < 0 else (p2, -1)
        
        while p1<=p2:
            if nums[p1]*(-d) > nums[p2]*(-d):
                ans[i] = nums[p1]
                p1+= 1
            else:
                ans[i] = nums[p2]
                p2 -= 1
            i += d
        return ans
