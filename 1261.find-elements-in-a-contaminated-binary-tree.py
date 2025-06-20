from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @leet start


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()

        if root:
            root.val = 0

        def dfs(node: Optional[TreeNode]) -> None:
            if node:
                self.seen.add(node.val)

                if node.left:
                    node.left.val = 2 * node.val + 1
                    node.left = dfs(node.left)
                if node.right:
                    node.right.val = 2 * node.val + 2
                    node.right = dfs(node.right)

        dfs(root)

    def find(self, target: int) -> bool:
        return target in self.seen


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# @leet end

