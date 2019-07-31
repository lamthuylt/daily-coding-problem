'''
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value. 
Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    

    def count_unival_subtrees(self):
        
        def is_unival_tree(root):                    
            if (root.left!=None and root.val!=root.left.val) or (root.right!=None and root.val!=root.right.val):
                return False  
            elif root.left==None and root.right==None:
                return True            
            if root.left!=None and root.right==None and root.val==root.left.val:
                return is_unival_tree(root.left)                        
            elif root.left==None and root.right!=None and root.val==root.right.val:
                return is_unival_tree(root.right)
            elif root.left!=None and root.right!=None and root.val==root.left.val==root.right.val:
                return is_unival_tree(root.left) and is_unival_tree(root.right)
            
        
#        count = 0
#        if root!=None and is_unival_tree(root):
#            count += 1               
#        if 
            
        return is_unival_tree(self)
           
        

if __name__ == '__main__':
    root = Node(0, Node(1), Node(0,Node(1,Node(1),Node(1)),Node(0))) 
    #root = Node(1, Node(1), Node(1,Node(1,Node(1),Node(1)),Node(1))) 
    print(root.count_unival_subtrees())
        