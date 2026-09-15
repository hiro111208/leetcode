# Step 3

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in t:
            if i < len(s) and s[i] == c:
                i += 1
        return i == len(s)
```

1回目: 分　秒

2回目: 分　秒

3回目: 分　秒
