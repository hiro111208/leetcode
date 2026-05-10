# Step 2

- 空間計算量を改善する

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                row[j] += row[j - 1]
        return row[n - 1]

```

時間計算量: $O(m \times n)$

空間計算量: $O(n)$
