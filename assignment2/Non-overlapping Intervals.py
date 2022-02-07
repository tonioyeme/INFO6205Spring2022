class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        intervals.sort(key = lambda x:x[1])
        upper = intervals[0][1]
        
        i = 1
        while i < len(intervals):
            if intervals[i][0] < upper:
                result += 1
                i += 1
            else:
                upper = intervals[i][1]
                i += 1
        return result