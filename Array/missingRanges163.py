# 163. Missing Ranges 
'''
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
'''
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        
        pre, ans = lower - 1, []
        nums.append(upper + 1)
        for num in nums:
            if num == pre + 2:
                ans.append(str(pre + 1))
            elif num > pre + 2:
                ans.append(str(pre + 1) + "->" + str(num - 1))
            pre = num
        return ans

