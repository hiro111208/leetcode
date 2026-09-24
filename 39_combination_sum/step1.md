# Step 1

## Approach 1

### Explanation

### Code

```python
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(index, cur, total):
            if total == target:
                result.append(cur.copy())
                return
            if total > target or index >= len(candidates):
                return
            backtrack(index, cur + [candidates[index]], total + candidates[index])
            backtrack(index + 1, cur, total)

        backtrack(0, [], 0)

        return result
```

時間計算量:

空間計算量:
