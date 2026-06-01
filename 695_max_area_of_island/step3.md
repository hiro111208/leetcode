# Step 3

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

1回目: 4分　0秒

2回目: 3分　41秒

3回目: 3分　9秒
