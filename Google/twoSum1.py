# 1. Two Sum
'''
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                ans.append(dic[target - num])
                ans.append(i)
            dic[num] = i
        return ans
'''