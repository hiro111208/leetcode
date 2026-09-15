# Step 1

## Approach 1

### Explanation

### Code

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        s_pointer = 0
        for character in t:
            if s[s_pointer] == character:
                s_pointer += 1
                if s_pointer == len(s):
                    return True
        return False
```

時間計算量: O(n)

空間計算量: O(1)
