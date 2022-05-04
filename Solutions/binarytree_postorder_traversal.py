class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        p = []
        if not root:
            return []
        p = p + self.postorderTraversal(root.left)
        p = p + self.postorderTraversal(root.right)
        p = p + [root.val]
        return p