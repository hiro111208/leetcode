# Step 2

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
            cur.append(candidates[index])
            backtrack(index, cur, total + candidates[index])
            cur.pop()
            backtrack(index + 1, cur, total)

        backtrack(0, [], 0)

        return result
```

時間計算量:

空間計算量:
