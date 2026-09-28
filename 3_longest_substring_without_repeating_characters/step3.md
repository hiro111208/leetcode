# Step 3

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in last_index:
                left = max(last_index[char] + 1, left)
            last_index[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len
```

1回目: 1分　54秒

2回目: 1分　17秒

3回目: 1分　36秒
