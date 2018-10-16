# 57. Insert Interval
'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i, j = 0, 0
        x, y = newInterval.start, newInterval.end
        
        while i < len(intervals):
            if x <= intervals[i].end:
                break
            i += 1
        
        while j < len(intervals):
            if y < intervals[j].start:
                break
            j += 1
        if i == j:
            intervals.insert(i, newInterval)
        else:
            intervals[i].start = min(intervals[i].start, x)
            intervals[i].end = max(intervals[j - 1].end, y)
            del intervals[i + 1: j]
        
        return intervals
    
    
    
    

