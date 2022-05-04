class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        if root is not None:
            inorder.extend(self.inorderTraversal(root.left))
            inorder.append(root.val)
            inorder.extend(self.inorderTraversal(root.right))
                
        return inorder