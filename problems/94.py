from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []

        output: list[int] = []

        # recursive solution

        # if root.left is not None:
        #     output += self.inorderTraversal(root.left)
        # output.append(root.val)
        # if root.right is not None:
        #     output += self.inorderTraversal(root.right)
        #

        # iterative solution

        nodes: list[TreeNode] = []
        curr_node: TreeNode | None = root

        while (len(nodes) != 0) or (curr_node is not None):
            while curr_node is not None:
                nodes.append(curr_node)
                curr_node = curr_node.left
            curr_node = nodes.pop()
            output.append(curr_node.val)
            curr_node = curr_node.right

        # Morris traversal

        # curr_node: TreeNode | None = root
        #
        # while curr_node is not None:
        #     if curr_node.left is None:
        #         output.append(curr_node.val)
        #         curr_node = curr_node.right
        #     else:
        #         temp_node: TreeNode = curr_node.left
        #         while temp_node.right is not None:
        #             temp_node = temp_node.right
        #         temp_node.right = curr_node
        #         temp_node.right.left = None
        #         curr_node = curr_node.left

        return output
