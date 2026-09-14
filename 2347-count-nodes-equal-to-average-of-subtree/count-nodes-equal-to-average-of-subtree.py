# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        #post-order dfs to calc subtrees then measure val of main node
        #dfs returns sum + node_count + propogate up running sum
        def dfs(node):
            #return sum + node count and node satisfying condition of 0
            if not node:
                return 0, 0, 0

            left_sum, left_count, left_ans = dfs(node.left)
            right_sum, right_count, right_ans = dfs(node.right)
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            sub_average = total_sum // total_count
            total_ans = left_ans + right_ans + (1 if node.val == sub_average else 0)
            return (total_sum, total_count, total_ans)

        return dfs(root)[2]