# Step 2

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_columns = len(grid[0])
        visited = set()
        max_area = 0

        def measure_island(r, c):
            if not (0 <= r < num_rows and 0 <= c < num_columns) or (r, c) in visited or grid[r][c] != 1:
                return 0
            visited.add((r, c))
            return 1 + measure_island(r + 1, c) + measure_island(r - 1, c) + measure_island(r, c + 1) + measure_island(r, c - 1)

        for r in range(num_rows):
            for c in range(num_columns):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, measure_island(r, c))

        return max_area

```

時間計算量: $O(mn)$

空間計算量: $O(mn)$

アルゴリズム最大実行時間(概算): 時間計算量 / Pythonの1秒あたりの計算ステップ数 -> $(50 \times 50) \div 10,000,000 = 0.000025 (s)$
