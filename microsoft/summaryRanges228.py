# 228. Summary Ranges
'''

Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
'''
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """


        
        ans = []
        if not nums:
            return ans
        
        start = 0
        i = 1
        while i < len(nums):
            if nums[i] - nums[start] != i - start:
                if i == start + 1:
                    ans.append(str(nums[start]))
                    start = i
                else:
                    ans.append(str(nums[start]) + '->' + str(nums[i - 1]))
                    start = i
            i += 1
        
        if i - 1 == start:
            ans.append(str(nums[start]))
        else:
            ans.append(str(nums[start]) + '->' + str(nums[i - 1]))
                    
        return ans

