# This problem is similar to problem #236, with the difference that node p and node q are not always in the binary tree.
# First do depth first search on the binary tree to find the nodes p and q. If either node does not exist, return null.
# If both p and q are in the binary tree, then do depth first search again to find the lowest common ancestor.
# Alternative Optimal Solution: no traversal of the binary tree is needed. Just use the binary tree property.
# Use post-order traversal: tranverse all the children of a node first, before returning to the parent
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        self.p_found = False
        self.q_found = False

        ans = self.dfs(root, p, q)
        
        return ans if self.q_found and self.p_found else None
    
    def dfs(self, node, p, q):
        if not node:
            return None
        l = self.dfs(node.left, p, q)
        r = self.dfs(node.right, p, q)

        if node == p or node == q:
            if node == p:
                self.p_found = True
            if node == q:
                self.q_found = True
            return node
        else:
            if l and r:
                return node
            else:
                return l or r