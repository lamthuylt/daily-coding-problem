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
        # Method 1 - multiple passes
        def is_unival_tree(root):                    
            if (root.left!=None and root.val!=root.left.val) or (root.right!=None and root.val!=root.right.val):
                return False  
            elif root.left==None and root.right==None:
                return True            
            elif root.left!=None and root.right==None and root.val==root.left.val:
                return is_unival_tree(root.left)                        
            elif root.left==None and root.right!=None and root.val==root.right.val:
                return is_unival_tree(root.right)
            elif root.left!=None and root.right!=None and root.val==root.left.val==root.right.val:
                return is_unival_tree(root.left) and is_unival_tree(root.right)

        def increment_count(root, count):
            if root!=None and is_unival_tree(root):
                count += 1               
            if root.left!=None:
                count = increment_count(root.left, count)
            if root.right!=None:
                count = increment_count(root.right, count)
            return count
        
        count = 0
        return increment_count(self, count)
    
    
    def count_unival_subtrees_2(self):
        # Method 2 - one pass
        # This method is based on the remark that all the nodes of a unival tree are roots of unival subtrees

        def is_unival_tree_and_count_nodes(root, nb_nodes):
            if (root.left!=None and root.val!=root.left.val) or (root.right!=None and root.val!=root.right.val):
                return False,_  
            elif root.left==None and root.right==None:
                return True, nb_nodes+1 
            if root.left!=None and root.right==None and root.val==root.left.val:
                return is_unival_tree_and_count_nodes(root.left, nb_nodes+1)                        
            elif root.left==None and root.right!=None and root.val==root.right.val:
                return is_unival_tree_and_count_nodes(root.right, nb_nodes+1)
            elif root.left!=None and root.right!=None and root.val==root.left.val==root.right.val:
                check_left, nb_nodes = is_unival_tree_and_count_nodes(root.left, nb_nodes+1)
                check_right, nb_nodes = is_unival_tree_and_count_nodes(root.right, nb_nodes)
                return (check_left and check_right), nb_nodes
        
        def increment_count(root, count):
            nb_nodes = 0
            is_unival, nb_nodes = is_unival_tree_and_count_nodes(root, nb_nodes)
            if is_unival == True:
                return count+nb_nodes
            else:
                if root.left != None:                
                    count = increment_count(root.left, count)
                if root.right != None:                    
                    count = increment_count(root.right, count)
                return count
        
        count = 0
        return increment_count(self, count)
    
if __name__ == '__main__':
    root = Node(0, Node(1), Node(0,Node(1,Node(1),Node(1)),Node(0))) 
    #root = Node(1, Node(1), Node(1,Node(1,Node(1),Node(1)),Node(1))) 
    print("Number of unival subtrees (method 1): {}".format(root.count_unival_subtrees()))
    print("Number of unival subtrees (method 2): {}".format(root.count_unival_subtrees_2()))
    """
        0
      /  \
     (1)  0
        /  \
       (1) (0)
      /  \
     (1) (1)
   """     