# 152. Maximum Product Subarray
'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp_max = [0]*len(nums)
        dp_min = [0]*len(nums)
        ans = float('-inf')
        for i in range(len(nums)):
            dp_max[i] = nums[i]
            dp_min[i] = nums[i]
            if i > 0:
                if nums[i] >= 0:
                    dp_max[i] = max(dp_max[i], nums[i]*dp_max[i - 1])
                    dp_min[i] = min(dp_min[i], nums[i]*dp_min[i - 1])
                else:
                    dp_max[i] = max(dp_max[i], nums[i]*dp_min[i - 1])
                    dp_min[i] = min(dp_min[i], nums[i]*dp_max[i - 1])                    
            ans = max(ans, dp_max[i])
        return ans

