#47. Permutations II
'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        if len(nums) == 1:
            return [nums]
        for numlis in self.permuteUnique(nums[1:]):
            for i in range(len(numlis) + 1):
                ans.append(numlis[:i] + [nums[0]] + numlis[i:])
                if i < len(numlis) and nums[0] == numlis[i]:
                    break
        return ans
        


