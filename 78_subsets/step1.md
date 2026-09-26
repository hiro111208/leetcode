# Step 1

## Approach 1

### Explanation

### Code

```python
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        def backtrack(index, cur):
            if index >= len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[index])
            backtrack(index + 1, cur)
            cur.pop()
            backtrack(index + 1, cur)
        backtrack(0, [])
        return res
```

時間計算量:

空間計算量:
