# Step 2

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

時間計算量: O(n)

空間計算量: O(min(n, Σ)) — Σ = charset size
