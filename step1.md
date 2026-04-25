# Step 1

## Recursive DFS (失敗)

- nodeがNoneだったら0を返す
- 左右最小の深さに1を足して返す

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
```

- 葉が片方にしかないとき、rootに0が返ってくる

時間計算量: O(n)

空間計算量: O(n)

## Iterative DFS

- nodeはNoneではないが、left, rightがNoneの場合に最小の深さを更新する

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        res = 10 ** 5
        stack = [[root, 1]]
        while stack:
            node, depth = stack.pop()
            if node:
                if node.left is None and node.right is None:
                    res = min(res, depth)
                else:
                    stack.append([node.left, depth + 1])
                    stack.append([node.right, depth + 1])
        return res
```

時間計算量: O(n)

空間計算量: O(n)
