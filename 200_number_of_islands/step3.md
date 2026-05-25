# Step 3

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        num_islands = 0

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < columns):
                return
            if grid[r][c] != "1" or (r, c) in visited:
                return
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r, c) not in visited:
                    num_islands += 1
                    dfs(r, c)

        return num_islands
```
1回目: 5分　9秒

2回目: 3分　25秒

3回目: 2分　57秒
