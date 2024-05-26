from collections import defaultdict, deque

class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
          
class Solution:
    def vertical_order(self, root):
        """
        Approach - Inorder Traversal
        - start from root taking row=0 and column = 0
        - when you go left, do row + 1 and column - 1 
        - when you go right, do row + 1 and column + 1
        - Append the node values to corresponding columns in a hashmap 
        - Iterate the hashmap column wise
        - sort the nodes at each column row-wise
        - return
        """
        column_map = defaultdict(list)
        def dfs(node, row, col):
            if node:
                column_map[col].append((row, node.val))
                dfs(node.left, row+1, col-1)
                dfs(node.right, row+1, col+1)
        dfs(root, 0, 0)
        mincol, maxcol = min(column_map), max(column_map)
        ans = []
        for col in range(mincol,maxcol+1):
            nodes = column_map[col]
            nodes.sort()
            nodes = [node for _, node in nodes]
            ans.append(nodes)
        return ans

class Solution1:
    def vertical_order(self, root):
        """
        Approach - Level Order Traversal
        - start from root taking row=0 and column = 0
        - when you go left child, do row + 1 and column - 1 
        - when you go right, do row + 1 and column + 1
        - Append the node values to corresponding columns in a hashmap 
        - Iterate the hashmap column wise
        - sort the nodes at each column row-wise
        - return
        """
        column_map = defaultdict(list)
        q = deque()
        row, col = 0, 0
        q.append((root, row, col))
        while q:
            node,row,col = q.popleft()
            column_map[col].append((row, node.val))
            if node.left: q.append((node.left, row+1, col-1))
            if node.right: q.append((node.right, row+1, col+1))
        mincol, maxcol = min(column_map), max(column_map)
        ans = []
        for col in range(mincol,maxcol+1):
            nodes = column_map[col]
            nodes.sort()
            nodes = [node for _, node in nodes]
            ans.append(nodes)
        return ans


if __name__=='__main__':
    """
    The vertical order traversal of a binary tree is a list of top-to-bottom orderings 
    for each column index starting from the leftmost column and ending on the rightmost column. 
    There may be multiple nodes in the same row and same column. 
    In such a case, sort these nodes by their values.
        1
       / \
      2   5
     / \  /
    3  6 4
    """
    t = TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(5,TreeNode(6)))
    print(Solution1().vertical_order(t))