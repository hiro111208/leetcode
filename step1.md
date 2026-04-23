# Step 1

- setとdictを用意する
- 各characterをsetに追加、初見ならdictにインデックスと一緒に追加
- characterが再び現れたらdictから削除
- ループが一周したら、dictでループし最小のインデックスを返す

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = set()
        unique_char_to_idx = dict()

        for idx, char in enumerate(s):
            if char in chars:
                unique_char_to_idx.pop(char, None)
            else:
                chars.add(char)
                unique_char_to_idx[char] = idx

        if len(unique_char_to_idx) == 0:
            return -1

        return min(unique_char_to_idx.values())
```

時間計算量: O(n)

空間計算量: O(n)
