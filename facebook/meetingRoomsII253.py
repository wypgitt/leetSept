# 253. Meeting Rooms II
'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
'''
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]
        
        start.sort()
        end.sort()
        s = e = 0
        ans = available = 0
        while s < len(start):
            if start[s] < end[e]:
                if available == 0:
                    ans += 1
                else:
                    available -= 1
                    
                s += 1
                
            else:
                available += 1
                e += 1
                
        return ans
        
