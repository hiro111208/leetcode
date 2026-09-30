# Step 1

## Approach 1

### Explanation

### Code

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

時間計算量:

空間計算量:
