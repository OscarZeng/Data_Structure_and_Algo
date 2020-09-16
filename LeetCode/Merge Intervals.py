class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1 or len(intervals) == 0:
            return intervals
        intervals.sort()
        ans = [intervals[0]]
        
        for i in range(1,len(intervals)):
            if ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                #Consider all kinds of conditions
                left, right = min(ans[-1][0], intervals[i][0]), max(ans[-1][1], intervals[i][1])
                newInterval = [left, right]
                ans.pop()
                ans.append(newInterval)
        return ans