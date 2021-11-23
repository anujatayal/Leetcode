# Given the root of a binary tree, invert the tree, and return its root.
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            if root.left!=None and root.right!=None:
                rootTemp=TreeNode()
                rootTemp=root.left
                root.left=root.right
                root.right=rootTemp
                self.invertTree(root.left)
                self.invertTree(root.right)
            elif root.left!=None and root.right==None:
                root.right=root.left
                root.left=None
                self.invertTree(root.right)
            elif root.left==None and root.right!=None:
                root.left=root.right
                root.right=None
                self.invertTree(root.left)
            return root
        return root            
            