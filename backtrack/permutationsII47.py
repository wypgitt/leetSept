# 47. Permutations II
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
        ans = [[]]
        
        for num in nums:
            temp = []
            for a in ans:
                for i in range(len(a) + 1):
                    temp.append(a[:i] + [num] + a[i:])
                    if i < len(a) and a[i] == num:
                        break
            ans = temp
        return ans
