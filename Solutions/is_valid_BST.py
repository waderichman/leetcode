class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def calc(node, curr_min, curr_max):
            if node is None:
                return True
            if node.val <= curr_min or node.val >= curr_max:
                return False
            left = calc(node.left, curr_min, node.val)
            right = calc(node.right, node.val, curr_max)
            return left and right
        return calc(root, float('-inf'), float('inf'))