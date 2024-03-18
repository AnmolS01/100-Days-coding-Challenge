# Problem Statement452. Minimum Number of Arrows to Burst Balloons

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Example 2:
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

#___________________________________________________________________________________CODE IS HERE____________________________________________________________________________________

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        arrows = 1
        if n==1:
            return 1
        for i in range(1, n):
            if points[i][0] > points[i-1][1]:
                arrows += 1
            else:
                points[i][0] = max(points[i][0], points[i-1][0])
                points[i][1] = min(points[i][1], points[i-1][1])
        return arrows
