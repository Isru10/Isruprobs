class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort(key=lambda x:x[1])
        arrow=1
        arrowpos=points[0][1]
        for start , end in points:
            if start>arrowpos:
                arrow+=1
                arrowpos=end
        return arrow 