# 128. Longest Consecutive Sequence
'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                ans = max(ans, current_streak)
        return ans
        
        

        

        '''
        if not nums:
            return 0
        
        nums.sort()
        
        ans = 1
        current_streak = 1
        
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                if nums[i - 1] == nums[i] - 1:
                    current_streak += 1
                else:
                    ans = max(ans, current_streak)
                    current_streak = 1
        return max(ans, current_streak)
 


        
        brute force
        ans = 0
        for num in nums:
            current_num = num
            current_streak = 1
            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1
            ans = max(ans, current_streak)
        return ans
        '''
