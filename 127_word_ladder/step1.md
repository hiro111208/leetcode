# Step 1

## Approach 1

### Explanation

### Code

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if not endWord in wordList:
            return 0
        wordList.append(beginWord)
        neis = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                neis[pattern].append(word)
        queue = deque([beginWord])
        visited = {beginWord}
        res = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for nei in neis[pattern]:
                        if not nei in visited:
                            visited.add(nei)
                            queue.append(nei)
            res += 1
        return 0
```

時間計算量:

空間計算量:
