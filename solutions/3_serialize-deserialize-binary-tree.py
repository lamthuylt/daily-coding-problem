"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self, root):
        s = []
        
        def encode(node):
            if node:
                s.append(node.val)
                encode(node.left)
                encode(node.right)
            else:
                s.append('#')

        encode(root)    
        return ' '.join(s)
        
    def deserialize(self, s):

        def decode(vals):
            val = next(vals)
            if val == '#':
                return None
            node = Node(val)
            node.left = decode(vals)
            node.right = decode(vals)
            return node
        
        vals = iter(s.split())
        return decode(vals)
        
        

if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert node.deserialize(node.serialize(node)).left.left.val == 'left.left'
    print('Serialize deserialize binary tree: {}'.format(node.deserialize(node.serialize(node)).left.left.val == 'left.left'))