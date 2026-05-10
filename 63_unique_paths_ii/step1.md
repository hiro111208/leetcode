# Step 1

- ある地点$grid[i][j]$に辿り着けるルートの数は$grid[i - 1][j]$に辿り着くルートの数と$grid[i][j - 1]$に辿り着くルートの数の和である

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])

        if obstacleGrid[M - 1][N - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        prev_row = [0] * N
        for i, cell in enumerate(obstacleGrid[0]):
            if cell == 0:
                prev_row[i] = 1
            else:
                break

        for i in range(1, M):
            new_row = [0] * N
            new_row[0] = prev_row[0] if obstacleGrid[i][0] == 0 else 0
            for j in range(1, N):
                if obstacleGrid[i][j] == 0:
                    new_row[j] = new_row[j - 1] + prev_row[j]
            prev_row = new_row
        return prev_row[N - 1]
```

時間計算量: $O(m \times n)$

空間計算量: $O(n)$
