# Step 3

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        boolean_list = [False] * (len(s) + 1)
        boolean_list[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i + len(word)] in wordDict:
                    boolean_list[i] = boolean_list[i + len(word)]
                if boolean_list[i]:
                    break
        return boolean_list[0]
```

1回目: 2分　18秒

2回目: 2分　9秒

3回目: 1分　54秒
