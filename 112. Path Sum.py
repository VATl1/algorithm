class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False

        if root.left is None and root.right is None:
            if root.val == targetSum:
                return True
            else:
                return False

        left_result = self.hasPathSum(root.left, targetSum - root.val)
        right_result = self.hasPathSum(root.right, targetSum - root.val)
        
        if left_result or right_result:
            return True
        return False