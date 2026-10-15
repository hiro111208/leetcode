# Step 3

```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [False] * n
        components = 0

        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            for neighbor in adj_list[node]:
                dfs(neighbor)

        for i in range(n):
            if visited[i]:
                continue
            components += 1
            dfs(i)

        return components
```

1回目: 2分　45秒

2回目: 2分　22秒

3回目: 2分　9秒
