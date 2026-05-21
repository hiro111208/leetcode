# Step 2

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

時間計算量: $O(mn)$

空間計算量: $O(mn)$

アルゴリズム最大実行時間(概算): 時間計算量 / Pythonの1秒あたりの計算ステップ数 -> $(10^4 \times 100) \div 10,000,000 = 0.1 (s)$
