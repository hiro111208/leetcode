# Step 2

- hashを2つ宣言する必要なかった

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        character_to_idx = dict()
        n = len(s)

        for idx, character in enumerate(s):
            if character in character_to_idx:
                character_to_idx[character] = n
            else:
                character_to_idx[character] = idx

        res = min(character_to_idx.values())
        return -1 if res == n else res
```
