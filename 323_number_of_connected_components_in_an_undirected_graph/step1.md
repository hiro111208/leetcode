# Step 1

## Approach 1

### Explanation

### Code

```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        res = 0
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for u in adj_list[node]:
                dfs(u)
        for i in range(n):
            if i in visited:
                continue
            res += 1
            dfs(i)
        return res
```

時間計算量:

空間計算量:
