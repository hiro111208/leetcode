# Step 3

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

1回目: 1分　31秒

2回目: 1分　40秒

3回目: 1分　29秒
