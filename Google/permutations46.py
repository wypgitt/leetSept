# 46. Permutations
'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


        ans = []
        
        visited = [False]*len(nums)
        
        self.backtrack(nums, ans, [], visited)
        return ans
        
    def backtrack(self, nums, ans, current, visited):
        if len(current) == len(nums):
            ans.append(list(current))
            return 
        
        for i, num in enumerate(nums):
            if visited[i] == False:
                visited[i] = True
                self.backtrack(nums, ans, current + [num], visited)
                visited[i] = False
                
        '''
        ans = [[]]
        
        for num in nums:
            ans = [l[:i] + [num] + l[i:] for l in ans for i in range(len(l) + 1)]
        return ans
	'''

        ans = [[]]
        
        for num in nums:
            temp = []
            for a in ans:
                for i in range(len(a) + 1):
                    temp.append(a[:i] + [num] + a[i:])
            ans = temp
        return ans
