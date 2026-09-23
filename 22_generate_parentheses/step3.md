# Step 3

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        result = []

        def backtrack(open_count, close_count):
            if open_count == close_count == n:
                result.append("".join(path))
                return

            if open_count < n:
                path.append("(")
                backtrack(open_count + 1, close_count)
                path.pop()
            if close_count < open_count:
                path.append(")")
                backtrack(open_count, close_count + 1)
                path.pop()

        backtrack(0, 0)
        return result
```

1回目: 2分　28秒

2回目: 2分　41秒

3回目: 2分　22秒
