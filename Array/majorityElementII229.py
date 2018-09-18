# 229. Majority Element II
'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        cnt1, cnt2, candidate1, candidate2 = 0, 0, 0, 1
        for num in nums:
            if num == candidate1:
                cnt1 +=1
            elif num == candidate2:
                cnt2 +=1
            elif cnt1 == 0:
                candidate1, cnt1 = num, 1
            elif cnt2 == 0:
                candidate2, cnt2 = num, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums)//3]
        
 # Boyer-Moore Majority Vote algorithm       
        
        

