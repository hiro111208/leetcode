# Step 3

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        signature_to_words = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for character in word:
                key[ord(character) - ord("a")] += 1
            signature_to_words[tuple(key)].append(word)
        return list(signature_to_words.values())

```

1回目: 1分　47秒

2回目: 1分　28秒

3回目: 1分　29秒
