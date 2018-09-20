# 349. Intersection of Two Arrays
'''

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

'''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """ 
        nums2.sort()
        ans = set()
        
        for num in nums1:
            n = self.helper(nums2, num)
            if n is not None:
                ans.add(n)
        return list(ans)
    
    def helper(self, arr, num):
        i, j = 0, len(arr) - 1
        while i <= j:
            mid = i + (j - i)//2
            if arr[mid] == num:
                return arr[mid]
            elif arr[mid] > num:
                j = mid - 1
            else:
                i = mid + 1


            
