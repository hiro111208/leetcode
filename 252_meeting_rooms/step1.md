# Step 1

- それぞれのinterval objectのstartからend値をsetに追加していく
- すでにsetに入っていたらFalseを返す
- ぜんぶ追加できてループを抜けたらTrueを返す

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
        times = set()
        for interval in intervals:
            for i in range(interval.start, interval.end):
                if i in times:
                    return False
                times.add(i)
        return True
```

時間計算量: $O(nm)$

空間計算量: $O(nm)$
