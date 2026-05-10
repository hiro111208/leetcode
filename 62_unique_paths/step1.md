# Step 1

- ある地点$grid[i][j]$に辿り着けるルートの数は$grid[i - 1][j]$に辿り着くルートの数と$grid[i][j - 1]$に辿り着くルートの数の和である

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * n] + [[1] + [0] * (n - 1)] * (m - 1)
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[m - 1][n - 1]
```

時間計算量: $O(m \times n)$

空間計算量: $O(m \times n)$
