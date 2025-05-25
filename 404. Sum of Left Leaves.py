class Solution(object):
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0

        total = 0
        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                total += root.left.val

        left_sum = self.sumOfLeftLeaves(root.left)
        right_sum = self.sumOfLeftLeaves(root.right)

        total = total + left_sum + right_sum
        return total