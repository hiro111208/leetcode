# Step 2

- 開始時間でintervalをソートし、intervalの開始時間が前のintervalの終了時間より早い場合はFalseを返す

```python
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        return True
```

時間計算量: $O(n\log n)$

空間計算量: $O(1)$
