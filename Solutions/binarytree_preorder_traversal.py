class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        p = []
        
        def dfs(node):
            if node:
                p.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return p