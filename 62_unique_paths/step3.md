# Step 3

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                row[j] += row[j - 1]
        return row[n - 1]
```

1回目: 1分　20秒

2回目: 1分　6秒

3回目: 1分　6秒
