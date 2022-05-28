class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        if left is False:
            return False
        else: 
            left = left + 1 
        if right is False:
            return False
        else:
            right = right + 1
        if abs(left - right) > 1:
            return False
        else:
            return max(left, right)