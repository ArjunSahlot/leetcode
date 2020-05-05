class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        xs = []
        ys = []
        for x,y in points:
            xs.append(x)
            ys.append(y)
        for i in range(0, len(points)-1):
            if abs(xs[i+1] - xs[i]) > abs(ys[i+1] - ys[i]):
                time += abs(xs[i+1] - xs[i])
            else:
                time += abs(ys[i+1] - ys[i])
        return time