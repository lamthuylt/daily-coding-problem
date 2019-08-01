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
        # Method 1
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

        def increment_count_unival_subtrees(root, count):
            if root!=None and is_unival_tree(root):
                count += 1               
            if root.left!=None:
                count = increment_count_unival_subtrees(root.left, count)
            if root.right!=None:
                count = increment_count_unival_subtrees(root.right, count)
            return count
        
        count = 0
        return increment_count_unival_subtrees(self, count)
    
    def count_unival_subtrees_2(self):
        # Method 2
        # This method is based on the remark that all the nodes of a unival subtree are roots of other unival subtrees
        return 0

if __name__ == '__main__':
    root = Node(0, Node(1), Node(0,Node(1,Node(1),Node(1)),Node(0))) 
    print("Number of unival subtrees: {}".format(root.count_unival_subtrees()))
    """
       0
      /  \
     (1)  0
        /   \
       (1)   (0)
      /   \
     (1)  (1)
   """     