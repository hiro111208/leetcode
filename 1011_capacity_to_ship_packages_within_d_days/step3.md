# Step 3

```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        def can_ship(cap):
            days_used, remaining = 1, cap
            for w in weights:
                if remaining < w:
                    days_used += 1
                    if days_used > days:
                        return False
                    remaining = cap
                remaining -= w
            return True

        while left <= right:
            cap = (left + right) // 2
            if can_ship(cap):
                right = cap - 1
            else:
                left = cap + 1

        return left
```

1回目: 3分　10秒

2回目: 2分　56秒

3回目: 2分　33秒
