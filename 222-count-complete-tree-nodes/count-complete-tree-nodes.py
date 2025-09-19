# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def countleft(node):
    l = 0
    while node:
        l +=1
        node = node.left
    return l

def countright(node):
    r = 0
    while node:
        r +=1
        node = node.right
    return r

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        left = countleft(root)
        right = countright(root)
        if left == right:
            return 2 ** left + -1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)    
           