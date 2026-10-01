# Step 3

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = helper(x, n // 2)
            res *= res
            return res * x if n % 2 else res
        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res
```

1回目: 1分　20秒

2回目: 1分　20秒

3回目: 1分　25秒
