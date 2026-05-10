# Step 2

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        number_of_rows = len(obstacleGrid)
        number_of_columns = len(obstacleGrid[0])

        prev_row = [0] * number_of_columns
        for i, cell in enumerate(obstacleGrid[0]):
            if cell == 0:
                prev_row[i] = 1
            else:
                break

        for r in range(1, number_of_rows):
            new_row = [0] * number_of_columns
            new_row[0] = prev_row[0] if obstacleGrid[r][0] == 0 else 0
            for c in range(1, number_of_columns):
                if obstacleGrid[r][c] == 0:
                    new_row[c] = new_row[c - 1] + prev_row[c]
            prev_row = new_row
        return prev_row[number_of_columns - 1]
```

時間計算量: $O(m \times n)$

空間計算量: $O(n)$
