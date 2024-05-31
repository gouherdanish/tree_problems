class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'T({self.val})'
    
class Solution:
    def maxHeight(self,root):
        def dfs(node):
            if node is None: return 0
            left_ht = dfs(node.left) 
            right_ht = dfs(node.right)
            return max(left_ht,right_ht) + 1
        return dfs(root)


if __name__=='__main__':
    t = TreeNode(1,TreeNode(2),TreeNode(3,TreeNode(4,TreeNode(5,TreeNode(6)))))
    # t = TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(5,TreeNode(6),TreeNode(7)))
    print(Solution().maxHeight(t))