# Step 2

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        number_of_rows = len(obstacleGrid)
        number_of_columns = len(obstacleGrid[0])

        row = [0] * number_of_columns
        for i, cell in enumerate(obstacleGrid[0]):
            if cell == 0:
                row[i] = 1
            else:
                break

        for r in range(1, number_of_rows):
            row[0] = row[0] if obstacleGrid[r][0] == 0 else 0
            for c in range(1, number_of_columns):
                if obstacleGrid[r][c] == 0:
                    row[c] += row[c - 1]
                else:
                    row[c] = 0
        return row[number_of_columns - 1]
```

時間計算量: $O(m \times n)$

空間計算量: $O(n)$
