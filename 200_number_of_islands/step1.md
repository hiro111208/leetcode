# Step 1

- 各セルで条件を満たす場合、dfsを行う
  - dfs
    - セルが1、まだ訪れていない、かつ範囲内だったら、counterを1増やして上下左右に行き、次のセルでも同じことを繰り返す

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        num_islands = 0

        def dfs(r, c):
            if (r, c) not in visited and r >= 0 and r < rows and c >= 0 and c < columns and grid[r][c] == "1":
                visited.add((r, c))
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r, c) not in visited:
                    num_islands += 1
                    dfs(r, c)

        return num_islands
```

時間計算量: $O(mn)$

空間計算量: $O(mn)$

アルゴリズム最大実行時間(概算): 時間計算量 / Pythonの1秒あたりの計算ステップ数 -> $(300 \times 300) \div 10,000,000 = 0.001 (s)$
