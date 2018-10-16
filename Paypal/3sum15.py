# 15. 3Sum
'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        if not nums:
            return ans
        nums.sort()
        
        
        for i in range(len(nums) - 2):
            j = len(nums) - 1
            if i == 0 or nums[i] != nums[i - 1]:
                
                k = i + 1
                record = []
                while k < j:
                    n = nums[i] + nums[k] + nums[j]
                    if n > 0:
                        j -= 1
                    elif n < 0:
                        k += 1
                    else:
                        if nums[k] not in record:
                            record.append(nums[k])
                            ans.append([nums[i], nums[k], nums[j]])
                        k += 1
                        j -= 1
        return ans
