import sys
import unittest
sys.path.append('/Users/pengyuxiong/workspace/dataStructure/avl_tree')
import avl_tree

class deletion_test(unittest.TestCase):
	def test_setUp(self):
		pass

	def test_delete_root(self):
		new_tree = avl_tree.AVL_Tree()
		new_tree.insert(0, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [0], 'tree does not match, insertion failed')
		new_tree.delete(0, new_tree.root)
		self.assertEqual(new_tree.root, None, 'wrong root data, deletion failed')

	def test_delete_neighbor_child(self):
		new_tree = avl_tree.AVL_Tree()
		new_tree.insert(0, new_tree.root)
		new_tree.insert(-1, new_tree.root)
		new_tree.insert(1, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-1, 0, 1], 'tree does not match, insertion failed')
		new_tree.delete(-1, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [0, 1], 'tree does not match, deletion failed')	
	
	def test_delete_leaf_node(self):
		new_tree = avl_tree.AVL_Tree()
		new_tree.insert(0, new_tree.root)
		new_tree.insert(-1, new_tree.root)
		new_tree.insert(1, new_tree.root)
		new_tree.insert(-2, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-2, -1, 0, 1], 'tree does not match, insertion failed')
		new_tree.delete(-2, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-1, 0, 1], 'tree does not match, deletion failed')

	def test_delete_root_with_children(self):
		new_tree = avl_tree.AVL_Tree()
		new_tree.insert(0, new_tree.root)
		new_tree.insert(-1, new_tree.root)
		new_tree.insert(1, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-1, 0, 1], 'tree does not match, insertion failed')
		new_tree.delete(0, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-1, 1], 'tree does not match, deletion faield')
		
	def test_delete_root_with_multiple_num(self):
		new_tree = avl_tree.AVL_Tree()
		new_tree.insert(0, new_tree.root)
		new_tree.insert(0, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [0], 'insertion failed, tree does not match')
		self.assertEqual(new_tree.root.num, 2, 'root.num does not match, insertion failed')
		new_tree.delete(0, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [0], 'deletion failed, tree does not match')
		self.assertEqual(new_tree.root.num, 1, 'deletion failed, num is not right')

	def test_delete_node_with_multiple_num_in_tree(self):
		new_tree = avl_tree.AVL_Tree()
		new_tree.insert(0, new_tree.root)
		new_tree.insert(1, new_tree.root)
		new_tree.insert(-1, new_tree.root)
		new_tree.insert(2, new_tree.root)
		new_tree.insert(2, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-1, 0, 1, 2], 'insertion failed, tree does not match')
		self.assertEqual(new_tree.root.right.right.num, 2, 'insertion failed, wrong node num')
		new_tree.delete(2, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-1, 0, 1, 2], 'deletion faield, tree does not matcj')
		self.assertEqual(new_tree.root.right.right.num, 1, 'deletion failed, wrong node num')

if __name__ == '__main__':
	unittest.main()
