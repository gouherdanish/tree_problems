from collections import defaultdict

class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def vertical_order(self, root):
        """
        Approach
        - start from root taking column = 0
        - when you go left, do column - 1 
        - when you go right, do column + 1
        - Append the node values to corresponding columns in a hashmap 
        - Iterate the hashmap column wise and print
        """
        column_map = defaultdict(list)
        def dfs(node, col):
            if node:
                column_map[col].append(node.val)
                dfs(node.left, col-1)
                dfs(node.right, col+1)
        dfs(root, 0)
        mincol, maxcol = min(column_map.keys()), max(column_map.keys())
        for col in range(mincol,maxcol+1):
            nodes = column_map[col]
            for node in nodes:
                print(node)

if __name__=='__main__':
    """
    The vertical order traversal of a binary tree is a list of top-to-bottom orderings 
    for each column index starting from the leftmost column and ending on the rightmost column. 
    There may be multiple nodes in the same row and same column. 
    In such case, print left to right
        1
       / \
      2   5
     / \  /
    3   4 6
    """
    t = TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(5,TreeNode(6)))
    Solution().vertical_order(t)