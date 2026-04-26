# Step 1

- non-tail recursionでできると思うが上手く言語化できない。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            merged_root = TreeNode(val=root2.val)
            merged_root.left = self.mergeTrees(None, root2.left)
            merged_root.right = self.mergeTrees(None, root2.right)
        elif root2 is None:
            merged_root = TreeNode(val=root1.val)
            merged_root.left = self.mergeTrees(root1.left, None)
            merged_root.right = self.mergeTrees(root1.right, None)
        else:
            merged_root = TreeNode(val=root1.val+root2.val)
            merged_root.left = self.mergeTrees(root1.left, root2.left)
            merged_root.right = self.mergeTrees(root1.right, root2.right)
        return merged_root
```

時間計算量: O(n)

空間計算量: O(n)

- 何も見ずに書けたものの、30分くらいかかってしまった。
