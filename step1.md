# Step 1

## Recursive DFS

- base case: nodeがNoneのとき0を返す
- recursive step: 左右のうちより深い方に1を足して返す

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
```

時間計算量: O(n)

空間計算量: O(n)

## Iterative DFS

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return max_depth
```

時間計算量: O(n)

空間計算量: O(n)

## BFS

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([[root, 1]])
        res = 0
        while queue:
            node, depth = queue.popleft()
            if node:
                res = depth
                queue.append([node.left, depth + 1])
                queue.append([node.right, depth + 1])
        return res
```

時間計算量: O(n)

空間計算量: O(n)
