"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda x: x.start)
        N = len(intervals)

        no_conflict = True

        for idx, tup in enumerate(intervals):
            start, end = tup.start, tup.end
            for j in range(idx+1, N):
                new_start = intervals[j].start
                if (new_start >= start) and (new_start < end):
                    no_conflict = False
                    break
        
        return no_conflict