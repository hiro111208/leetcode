# Step 2

- DPテーブルの変数、良い名付け方が思いつかない

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

時間計算量: $O(nmt)$

空間計算量: $O(n)$
