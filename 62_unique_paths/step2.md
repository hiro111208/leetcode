# Step 2

- 空間計算量を改善する

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_row = [1] * n
        for i in range(1, m):
            new_row = [1] + [0] * (n - 1)
            for j in range(1, n):
                new_row[j] = new_row[j - 1] + prev_row[j]
            prev_row = new_row
        return prev_row[n - 1]

```

時間計算量: $O(m \times n)$

空間計算量: $O(n)$
