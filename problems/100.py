from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if self.inorder_traversal(p) == self.inorder_traversal(q):
            print(self.inorder_traversal(p))
            print(self.inorder_traversal(q))
            return True
        return False

    def inorder_traversal(self, root: Optional[TreeNode]) -> list[int | None]:
        if root is None:
            return []

        output: list[int | None] = []
        nodes: list[TreeNode] = []
        curr_node: TreeNode | None = root

        print(root)

        while (len(nodes) != 0) or (curr_node is not None):
            while curr_node is not None:
                nodes.append(curr_node)
                curr_node = curr_node.left
            # empty left node
            output.append(None)
            curr_node = nodes.pop()
            output.append(curr_node.val)
            curr_node = curr_node.right
            print(output)

        return output
