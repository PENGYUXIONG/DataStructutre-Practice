import sys
import unittest
sys.path.append('/Users/pengyuxiong/workspace/dataStructure/avl_tree')
import avl_tree
class rotation_tests(unittest.TestCase):
  def test_setUp(self):
    pass
  
    '''
        bst                      avl  
          0                        0    
        /   \                     /  \ 
        -1    1                  -2   1
        /                       /  \ 
      -2                       -3  -1
      /
      -3 
    '''
  def test_left_type(self):
    new_tree = avl_tree.AVL_Tree()
    new_tree.insert(0, new_tree.root)
    new_tree.insert(-1, new_tree.root)
    new_tree.insert(1, new_tree.root)
    new_tree.insert(-2, new_tree.root)
    new_tree.insert(-3, new_tree.root)
    self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-3,-2,-1,0,1], 'right rotation failed, tree does not match')
    self.assertEqual(new_tree.root.data, 0, 'wrong root data')
    self.assertEqual(new_tree.root.left.data, -2, 'wrong node data')
    self.assertEqual(new_tree.root.right.data, 1, 'wrong leaf data')
    self.assertEqual(new_tree.root.right.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.right.right, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.left.left.data, -3, 'wrong leaf data')
    self.assertEqual(new_tree.root.left.left.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.left.left.right, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.left.right.data, -1, 'wrong leaf data')
    self.assertEqual(new_tree.root.left.right.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.left.right.right, None, 'extra node under leaf')
    

  def test_right_type(self):
    '''
      bst                            avl
        0                             0
      /   \                          / \ 
    -1     1                        -1  2
            \                         / \ 
              2                       1   3
                \                      
                3
    '''
    new_tree = avl_tree.AVL_Tree()
    new_tree.insert(0, new_tree.root)
    new_tree.insert(-1, new_tree.root)
    new_tree.insert(1, new_tree.root)
    new_tree.insert(2, new_tree.root)
    new_tree.insert(3, new_tree.root)
    self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-1, 0, 1, 2, 3], 'left rotation failed, tree does not match')
    self.assertEqual(new_tree.root.data, 0, 'wrong root data')
    self.assertEqual(new_tree.root.left.data, -1, 'wrong leaf data')
    self.assertEqual(new_tree.root.left.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.left.right, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.right.data, 2, 'wrong node data')
    self.assertEqual(new_tree.root.right.left.data, 1, 'wrong leaf data')
    self.assertEqual(new_tree.root.right.left.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.right.left.right, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.right.right.data, 3, 'wrong leaf data')
    self.assertEqual(new_tree.root.right.right.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.right.right.right, None, 'extra node under leaf')

  def test_left_left_type(self):
    '''
          bst                      avl
            0                       -1
          /   \                   /    \  
        -1     1                -2      0
        / \                    /  \    /  \ 
      -2 -0.5                 -3 -1.5 -0.5 1
      / \                      
      -3 -1.5                 
    '''
    new_tree = avl_tree.AVL_Tree()
    new_tree.insert(0, new_tree.root)
    new_tree.insert(-1, new_tree.root)
    new_tree.insert(1, new_tree.root)
    new_tree.insert(-2, new_tree.root)
    new_tree.insert(-0.5, new_tree.root)
    new_tree.insert(-3, new_tree.root)
    new_tree.insert(-1.5, new_tree.root)
    self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-3, -2, -1.5, -1, -0.5, 0, 1], 
    'right rotation failed, tree does not match')
    self.assertEqual(new_tree.root.data, -1, 'wrong root data')
    self.assertEqual(new_tree.root.left.data, -2, 'wrong node data')
    self.assertEqual(new_tree.root.right.data, 0, 'wrong node data')
    self.assertEqual(new_tree.root.left.left.data, -3, 'wrong leaf data')
    self.assertEqual(new_tree.root.left.left.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.left.left.right, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.left.right.data, -1.5, 'wrong leaf data')
    self.assertEqual(new_tree.root.left.right.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.left.right.right, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.right.left.data, -0.5, 'wrong leaf data')
    self.assertEqual(new_tree.root.right.left.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.right.left.right, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.right.right.data, 1, 'wrong leaf data')
    self.assertEqual(new_tree.root.right.right.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.right.right.right, None, 'extra node under leaf')

  def test_right_right_type(self):
    '''
           BST                                AVL
            0                                  1
           / \                               /    \ 
          -1   1                            0      2
              / \                          / \    / \ 
             0.5 2                        -1 0.5 1.5 3
                / \ 
               1.5 3
    '''
    new_tree = avl_tree.AVL_Tree()
    new_tree.insert(0, new_tree.root)
    new_tree.insert(-1, new_tree.root)
    new_tree.insert(1, new_tree.root)
    new_tree.insert(0.5, new_tree.root)
    new_tree.insert(2, new_tree.root)
    new_tree.insert(1.5, new_tree.root)
    new_tree.insert(3, new_tree.root)
    self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-1, 0, 0.5, 1, 1.5, 2, 3])
    self.assertEqual(new_tree.root.data, 1, 'wrong root data')
    self.assertEqual(new_tree.root.left.data, 0, 'wrong node data')
    self.assertEqual(new_tree.root.right.data, 2, 'wrong node data')
    self.assertEqual(new_tree.root.left.left.data, -1, 'wrong leaf data')
    self.assertEqual(new_tree.root.left.left.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.left.left.right, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.left.right.data, 0.5, 'wrong leaf data')
    self.assertEqual(new_tree.root.left.right.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.left.right.right, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.right.left.data, 1.5, 'wrong leaf data')
    self.assertEqual(new_tree.root.right.left.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.right.left.right, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.right.right.data, 3, 'wrong leaf data')
    self.assertEqual(new_tree.root.right.right.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.right.right.right, None, 'extra node under leaf')

  def test_left_right_type(self):
    '''
        BST                   AVL                          AVL
         0                     0                          -0.5
       /   \                  / \                      /         \ 
      -1    1               -0.5  1                  -1           0
     / \           ->       /  \           ->        / \         / \ 
   -2 -0.5                 -1  -0.25               -2 -0.75  -0.25  1
      /  \                 / \                        
  -0.75 -0.25            -2  -0.75                      
    '''
    new_tree = avl_tree.AVL_Tree()
    new_tree.insert(0, new_tree.root)
    new_tree.insert(-1, new_tree.root)
    new_tree.insert(1, new_tree.root)
    new_tree.insert(-2, new_tree.root)
    new_tree.insert(-0.5, new_tree.root)
    new_tree.insert(-0.75, new_tree.root)
    new_tree.insert(-0.25, new_tree.root)
    self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-2, -1, -0.75, -0.5, -0.25, 0, 1],
     'perform left rotation first then right rotation, one of the two operations failed, tree does not match')
    self.assertEqual(new_tree.root.data, -0.5, 'wrong root data')
    self.assertEqual(new_tree.root.left.data, -1, 'wrong node data')
    self.assertEqual(new_tree.root.right.data, 0, 'wrong node data')
    self.assertEqual(new_tree.root.left.left.data, -2, 'wrong leaf data')
    self.assertEqual(new_tree.root.left.left.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.left.left.right, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.left.right.data, -0.75, 'wrong leaf data')
    self.assertEqual(new_tree.root.left.right.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.left.right.right, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.right.left.data, -0.25, 'wrong leaf data')
    self.assertEqual(new_tree.root.right.left.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.right.left.right, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.right.right.data, 1, 'wrong leaf data')
    self.assertEqual(new_tree.root.right.right.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.right.right.right, None, 'extra node under leaf')

  def test_right_left_type(self):
    '''
          BST                   AVL                         
           0                     0                                0.5
         /   \                  / \                            /      \ 
        -1    1        ->      -1  0.5             ->         0         1
             /  \                  /  \                      / \      /   \ 
           0.5   2               0.25  1                   -1 0.25   0.75  2
           / \                        /  \ 
        0.25 0.75                   0.75  2
    '''
    new_tree = avl_tree.AVL_Tree()
    new_tree.insert(0, new_tree.root)
    new_tree.insert(-1, new_tree.root)
    new_tree.insert(1, new_tree.root)
    new_tree.insert(0.5, new_tree.root)
    new_tree.insert(2, new_tree.root)
    new_tree.insert(0.25, new_tree.root)
    new_tree.insert(0.75, new_tree.root)
    self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-1, 0, 0.25, 0.5, 0.75, 1, 2], 
    'right rotate first then left rotate, tree does not match, one of the two operations failed')
    self.assertEqual(new_tree.root.data, 0.5, 'wrong root data')
    self.assertEqual(new_tree.root.left.data, 0, 'wrong node data')
    self.assertEqual(new_tree.root.right.data, 1, 'wrong node data')
    self.assertEqual(new_tree.root.left.left.data, -1, 'wrong leaf data')
    self.assertEqual(new_tree.root.left.left.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.left.left.right, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.left.right.data, 0.25, 'wrong leaf data')
    self.assertEqual(new_tree.root.left.right.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.left.right.right, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.right.left.data, 0.75, 'wrong leaf data')
    self.assertEqual(new_tree.root.right.left.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.right.left.right, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.right.right.data, 2, 'wrong leaf data')
    self.assertEqual(new_tree.root.right.right.left, None, 'extra node under leaf')
    self.assertEqual(new_tree.root.right.right.right, None, 'extra node under leaf')

if __name__ == '__main__':
  unittest.main()