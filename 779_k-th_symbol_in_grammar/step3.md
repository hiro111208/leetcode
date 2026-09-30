# Step 3

```python
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        cur = 0
        l, r = 1, 2 ** (n - 1)
        for _ in range(n - 1):
            mid = (l + r) // 2
            if k <= mid:
                r = mid
            else:
                l = mid + 1
                cur = 0 if cur else 1
        return cur
```

1回目: 1分　20秒

2回目: 1分　10秒

3回目: 1分　5秒
