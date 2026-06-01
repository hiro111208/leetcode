# Step 1

- 各セルで１かつ訪れていなかったらdfsを行う
  - dfs
    - セルがgridの外、すでに訪れている、もしくは1でない場合は0を返す
    - セルが1だったら、隣接するセルのdfsの戻り値に1を足した値を返す

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_length = len(grid)
        column_length = len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r, c):
            if not (0 <= r < row_length and 0 <= c < column_length) or (r, c) in visited or grid[r][c] != 1:
                return 0
            visited.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(row_length):
            for c in range(column_length):
                max_area = max(max_area, dfs(r, c))

        return max_area
```

時間計算量: $O(mn)$

空間計算量: $O(mn)$

アルゴリズム最大実行時間(概算): 時間計算量 / Pythonの1秒あたりの計算ステップ数 -> $(50 \times 50) \div 10,000,000 = 0.000025 (s)$
