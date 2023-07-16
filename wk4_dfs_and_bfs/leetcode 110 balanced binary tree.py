# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getHeight(root: TreeNode) -> int:
            if root is None:
                return 0
            leftTreeHeight = getHeight(root.left)
            if leftTreeHeight == -1:
                return -1
            rightTreeHeight = getHeight(root.right)
            if rightTreeHeight == -1:
                return -1
            
            if abs(rightTreeHeight - leftTreeHeight) > 1:
                return -1
            else:
                return (1 + max(rightTreeHeight, leftTreeHeight))

        result = getHeight(root)
        if result == -1:
            return False
        else:
            return True            

            