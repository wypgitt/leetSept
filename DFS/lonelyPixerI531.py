# 531. Lonely Pixel I

'''
Given a picture consisting of black and white pixels, find the number of black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

Example:
Input: 
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

Output: 3
Explanation: All the three 'B's are black lonely pixels.
Note:
The range of width and height of the input 2D array is [1,500].
'''
class Solution:
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        if not picture:
            return 0
        count = 0
        for p in zip(*picture):
            if p.count('B') == 1:
                count += 1
        print(count)
        for p in picture:
            if p.count('B') > 1:
                count -= p.count('B')
        return count if count > 0 else 0
        

