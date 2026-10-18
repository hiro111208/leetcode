# Step 2

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        pattern_words = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                pattern_words[pattern].append(word)
        queue = deque([beginWord])
        visited = {beginWord}
        length = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return length
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for neighbor in pattern_words[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            length += 1
        return 0
```

時間計算量: O(N \* M^2)

空間計算量: O(N \* M^2)
