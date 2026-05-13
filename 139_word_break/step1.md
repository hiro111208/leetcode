# Step 1

- わからなかったので[NeetCodeの解説](https://www.youtube.com/watch?v=Sx9NNgInc3A)を見た
  - 末尾から見て「ここから先を辞書の語で切れるか」を`boolean_list[i]`に記録するDP
  - 空文字は `True`（`boolean_list[len(s)]`）。各位置 `i` で、辞書の語が `s` の先頭（`i` から）に合えば、その語の直後 `i+len(word)` が `True` なら `i` も `True`。最後に `boolean_list[0]` が答え。

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
