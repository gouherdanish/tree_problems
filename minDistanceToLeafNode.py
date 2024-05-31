class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'T({self.val})'
    
class Solution:
    """
    Approach - Inorder
    - check if current node is a leaf
        - if yes, find its depth from root and compare with min
        - if no, check next
    """
    def minDistanceToLeafNode(self,root):
        def dfs(node):
            if node is None: return float('inf')
            if node.left is None and node.right is None: return 0
            left_leaf_dist = dfs(node.left)
            right_leaf_dist = dfs(node.right)
            return min(left_leaf_dist,right_leaf_dist) + 1
        
        if not root: return 0
        return dfs(root)



if __name__=='__main__':
    # t = TreeNode(1,TreeNode(2,TreeNode(4)),TreeNode(3))
    # t = TreeNode(1,TreeNode(2),TreeNode(3,TreeNode(4,TreeNode(5,TreeNode(6)))))
    t = TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(5,TreeNode(6),TreeNode(7)))
    print(Solution().minDistanceToLeafNode(t))