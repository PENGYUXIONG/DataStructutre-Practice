import sys
import unittest
sys.path.append('/Users/pengyuxiong/workspace/dataStructure/red_black_tree')
import red_black_tree

class insertion_deletion_tests(unittest.TestCase):
	def test_setup(self):
		pass
	def test_simple_bst_insertion_deletion(self):
		'''
				0	(B)
			 / \  
			-1  1
		'''
		new_tree = red_black_tree.red_black_tree()
		new_tree.insert(0, new_tree.root)
		new_tree.insert(-1, new_tree.root)
		new_tree.insert(1, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-1, 0, 1],
		'insertion failed, tree does not match')
		self.assertEqual(new_tree.root.data, 0, 'wrong root data')
		self.assertEqual(new_tree.root.left.data, -1, 'wrong leaf data')
		self.assertEqual(new_tree.root.right.data, 1, 'wrong data')
		self.assertEqual(new_tree.root.color, 'black', 'wrong root color')
		self.assertEqual(new_tree.root.left.color, 'red', 'wrong leaf color')
		self.assertEqual(new_tree.root.right.color, 'red', 'wrong leaf color')
		new_tree.delete(0, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-1, 1], 'insertion failed, tree does not match')
		self.assertEqual(new_tree.root.color, 'black', 'wrong root color')
		self.assertEqual(new_tree.root.data, 1, 'wrong root data')
		self.assertEqual(new_tree.root.left.color, 'red', 'wrong leaf color')
		self.assertEqual(new_tree.root.left.data, -1, 'wrong leaf data')
		new_tree.delete(1, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-1])
		self.assertEqual(new_tree.root.color, 'black', 'wrong root color')
		self.assertEqual(new_tree.root.data, -1, 'wrong root data')

	def test_left_insertion(self):
		'''
				 bst
					0														  0 (B)
				/   \ 											  /   \ 
			 -1    1   			->       			-2(B)  1 (B)
			/  													  / \ 
		 -2														 -3 -1
		/
	 -3  
		'''
		new_tree = red_black_tree.red_black_tree()
		new_tree.insert(0, new_tree.root)
		new_tree.insert(-1, new_tree.root)
		new_tree.insert(1, new_tree.root)
		new_tree.insert(-2, new_tree.root)
		new_tree.insert(-3, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-3, -2, -1, 0, 1],
		'insertion failed, tree does not match')
		self.assertEqual(new_tree.root.data, 0, 'wrong root data')
		self.assertEqual(new_tree.root.left.data, -2, 'wrong node data')
		self.assertEqual(new_tree.root.right.data, 1, 'wrong leaf data')
		self.assertEqual(new_tree.root.left.left.data, -3, 'wrong leaf data')
		self.assertEqual(new_tree.root.left.right.data, -1, 'wrong leaf data')
		self.assertEqual(new_tree.root.color, 'black', 'wrong root color')
		self.assertEqual(new_tree.root.left.color, 'black', 'wrong node color')
		self.assertEqual(new_tree.root.right.color, 'black', 'wrong node color')
		self.assertEqual(new_tree.root.left.left.color, 'red', 'wrong leaf color')
		self.assertEqual(new_tree.root.left.right.color, 'red', 'wrong leaf color')
		new_tree.delete(-1, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-3, -2, 0, 1], 'deletion failed, tree does not match')
		new_tree.delete(-2, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-3, 0, 1])
		self.assertEqual(new_tree.root.data, 0, 'wrong root data')
		self.assertEqual(new_tree.root.color, 'black', 'wrong root color')
		self.assertEqual(new_tree.root.right.data, 1, 'wrong leaf data')
		self.assertEqual(new_tree.root.right.color, 'black', 'wrong leaf color')
		self.assertEqual(new_tree.root.left.data, -3, 'wrong leaf data')
		self.assertEqual(new_tree.root.left.color, 'black', 'wrong leaf color')

	def test_right_insertion(self):
		'''
						0																0 (B)
					 / \ 														/   \ 
					-1  1													 -1(B) 2 (B)
						   \           ->									/  \ 
								2														 1    3 
								 \ 
								  3
		'''

		new_tree = red_black_tree.red_black_tree()
		new_tree.insert(0, new_tree.root)
		new_tree.insert(-1, new_tree.root)
		new_tree.insert(1, new_tree.root)
		new_tree.insert(2, new_tree.root)
		new_tree.insert(3, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-1, 0, 1, 2, 3],
		'insertion failed, tree does not match')
		self.assertEqual(new_tree.root.data, 0, 'wrong root data')
		self.assertEqual(new_tree.root.color, 'black', 'wrong root color')
		self.assertEqual(new_tree.root.left.data, -1, 'wrong leaf data')
		self.assertEqual(new_tree.root.left.color, 'black', 'wrong leaf color')
		self.assertEqual(new_tree.root.right.data, 2, 'wrong node data')
		self.assertEqual(new_tree.root.right.color, 'black', 'wrong node color')
		self.assertEqual(new_tree.root.right.left.data, 1, 'wrong leaf data')
		self.assertEqual(new_tree.root.right.left.color, 'red', 'wrong leaf color')
		self.assertEqual(new_tree.root.right.right.data, 3, 'wrong leaf data')
		self.assertEqual(new_tree.root.right.right.color, 'red', 'wrong leaf color')
		new_tree.delete(2, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-1, 0, 1, 3], 'deletion failed, tree does not match')
		new_tree.delete(0, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-1, 1, 3], 'deletion failed, tree does not match')

	def test_recolor_case(self):
		'''
				0	(B)   					   0 (B)
			/   \ 							 /   \ 
		 -1(B) 1(B)	  			  -1    1 (B)
		/  \         ->      /  \ 
	 -2  -0.5						-2(B) -0.5(B) 
	/   	       				/ 			 
-3  								 -3	
		'''
		new_tree = red_black_tree.red_black_tree()
		new_tree.insert(0, new_tree.root)
		new_tree.insert(-1, new_tree.root)
		new_tree.insert(1, new_tree.root)
		new_tree.insert(-2, new_tree.root)
		new_tree.insert(-0.5, new_tree.root)
		new_tree.insert(-3, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-3,-2,-1,-0.5,0,1],
		'insert failed, tree does not match')
		self.assertEqual(new_tree.root.data, 0, 'wrong root data')
		self.assertEqual(new_tree.root.color, 'black', 'wrong root color')
		self.assertEqual(new_tree.root.left.data, -1, 'wrong node data')
		self.assertEqual(new_tree.root.left.color, 'red', 'wrong node color')
		self.assertEqual(new_tree.root.right.data, 1, 'wrong leaf data')
		self.assertEqual(new_tree.root.right.color, 'black', 'wrong leaf color')
		self.assertEqual(new_tree.root.left.left.data, -2, 'wrong node data')
		self.assertEqual(new_tree.root.left.left.color, 'black', 'wrong node color')
		self.assertEqual(new_tree.root.left.right.data, -0.5, 'wrong leaf data')
		self.assertEqual(new_tree.root.left.right.color, 'black', 'wrong leaf color')
		self.assertEqual(new_tree.root.left.left.left.data, -3, 'wrong leaf data')
		self.assertEqual(new_tree.root.left.left.left.color, 'red', 'wrong leaf color')
		new_tree.delete(-1, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-3, -2, -0.5, 0, 1], 'deletion failed, tree does not match')

	def test_left_left_insertion(self):
		'''
					 0(B)														0(B)										   -1(B)
					 /  \ 												/   \  									 /		      \ 
				  -1   1 (B)  								 -1    1(B)								-2   		      0
				 /  \             ->					/  \            ->			 /  \				 /    \ 
			 -2(B) -0.5(B)								 -2   -0.5(B)					-3(B)	-1.5(B)	-0.5(B) 1(B)
			 / \ 													/  \     								 /
			-3 -1.5											-3(B) -1.5(B)						  -4
		 /														 /
		-4														-4
		'''
		new_tree = red_black_tree.red_black_tree()
		new_tree.insert(0, new_tree.root)
		new_tree.insert(-1, new_tree.root)
		new_tree.insert(1, new_tree.root)
		new_tree.insert(-2, new_tree.root)
		new_tree.insert(-0.5, new_tree.root)
		new_tree.insert(-3, new_tree.root)
		new_tree.insert(-1.5, new_tree.root)
		new_tree.insert(-4, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-4,-3,-2,-1.5,-1,-0.5,0,1],
		'right rotation failed, tree does not match')
		self.assertEqual(new_tree.root.data, -1, 'wrong root data')
		self.assertEqual(new_tree.root.color, 'black', 'wrong root color')
		self.assertEqual(new_tree.root.left.data, -2, 'wrong node data')
		self.assertEqual(new_tree.root.left.color, 'red', 'wrong node color')
		self.assertEqual(new_tree.root.right.data, 0, 'wrong node data')
		self.assertEqual(new_tree.root.right.color, 'red', 'wrong node color')
		self.assertEqual(new_tree.root.left.left.data, -3, 'wrong node data')
		self.assertEqual(new_tree.root.left.left.color, 'black', 'wrong node color')
		self.assertEqual(new_tree.root.left.right.data, -1.5, 'wrong leaf data')
		self.assertEqual(new_tree.root.left.right.color, 'black', 'wrong leaf color')
		self.assertEqual(new_tree.root.right.left.data, -0.5, 'wrong leaf data')
		self.assertEqual(new_tree.root.right.left.color, 'black', 'wrong leaf color')
		self.assertEqual(new_tree.root.right.right.data, 1, 'wrong leaf data')
		self.assertEqual(new_tree.root.right.right.color, 'black', 'wrong leaf color')
		self.assertEqual(new_tree.root.left.left.left.data, -4, 'wrong leaf data')
		self.assertEqual(new_tree.root.left.left.left.color, 'red', 'wrong leaf color')
		new_tree.delete(-0.5, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-4, -3, -2, -1.5, -1, 0, 1], 'deletion failed, tree does not match')

	def test_left_right_insertion(self):
		'''
					bst
						0														  0 (B)																			0(B)									0(B)
					/   \ 											  /   \ 								 										 /  \ 								 / \ 
				-1    1   			->       			-2(B)  1 (B)        ->                   	  -2 1(B)      ->       -2  1(B)
				/  													  / \ 								  										  / \ 								 /  \ 
			-2														 -3 -1																		-3(B)  -1(B)	  			 -3(B) -1(B)
			/																								   											  										 				/ \ 
		-3  																																		 							 							 -1.5 -0.5

						0(B)														 0(B)														 0(B)											    -1(B)
					/     \ 												 /      \ 											  /     \ 									/          \ 
				-2       1(B)										  -2      1(B)									   -1     1(B)							 -2            0
			 /  \              ->							/    \                  -> 			  /  \                ->	 /   \ 			   /   \ 
		-3(B) -1(B)										 -3(B)     -1												  -2  -0.5(B) 						-3(B) -1.5(B) -0.5(B) 1(B)
					/  \ 															/   \ 										 /	 \		  \     								   				\ 
				-1.5 -0.5											 -1.5(B) -0.5(B)							-3(B) -1.5(B) -0.25					 								 -0.25																							
																									\ 
																								 -0.25
		'''
		new_tree = red_black_tree.red_black_tree()
		new_tree.insert(0, new_tree.root)
		new_tree.insert(-1, new_tree.root)
		new_tree.insert(1, new_tree.root)
		new_tree.insert(-2, new_tree.root)
		new_tree.insert(-3, new_tree.root)
		new_tree.insert(-1.5, new_tree.root)
		new_tree.insert(-0.5, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-3, -2, -1.5, -1, -0.5, 0, 1],
		'insertion failed, tree does not match')
		new_tree.insert(-0.25, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-3, -2, -1.5, -1, -0.5, -0.25, 0, 1], 
		'insertion failed, tree does not match')
		self.assertEqual(new_tree.root.data, -1, 'wrong root data')
		self.assertEqual(new_tree.root.color, 'black', 'wrong root color')
		self.assertEqual(new_tree.root.left.data, -2, 'wrong node data')
		self.assertEqual(new_tree.root.left.color, 'red', 'wrong node color')
		self.assertEqual(new_tree.root.right.data, 0, 'wrong node data')
		self.assertEqual(new_tree.root.right.color, 'red', 'wrong node color')
		self.assertEqual(new_tree.root.left.left.data, -3, 'wrong leaf data')
		self.assertEqual(new_tree.root.left.left.color, 'black', 'wrong leaf color')
		self.assertEqual(new_tree.root.left.right.data, -1.5, 'wrong leaf data')
		self.assertEqual(new_tree.root.left.right.color, 'black', 'wrong lead color')
		self.assertEqual(new_tree.root.right.left.data, -0.5, 'wrong node data')
		self.assertEqual(new_tree.root.right.left.color, 'black', 'wrong node color')
		self.assertEqual(new_tree.root.right.right.data, 1, 'wrong leaf data')
		self.assertEqual(new_tree.root.right.right.color, 'black', 'wrong leaf color')
		self.assertEqual(new_tree.root.right.left.right.data, -0.25, 'wrong leaf data')
		self.assertEqual(new_tree.root.right.left.right.color, 'red', 'wrong leaf color')

	def test_right_right_insertion(self):
		'''
						0																0 (B)											 0(B)												0(B)
					 / \ 														/   \ 											/  \ 											/     \ 
					-1  1													 -1(B) 2 (B)							 -1(B)  2										-1(B)    2
						   \           ->									/  \         -> 					 /  \      ->									/  \ 
								2														 1    3 									 1(B) 3(B)										1(B) 4(B)
								 \ 																													 \ 													/  \ 
								  3																														4												 3    5
						
					 0(B)														      2(B)		
					 /   \ 														  /      \ 
				-1(B)   2													   0        4
							 /  \              ->        /  \	     /  \   
						 1(B)  4										-1(B)	1(B) 3(B)	 5(B)
								 /   \ 												        		 \ 
 							 3(B) 5(B)														  			6
										  \ 
											 6
		'''
		new_tree = red_black_tree.red_black_tree()
		new_tree.insert(0, new_tree.root)
		new_tree.insert(-1, new_tree.root)
		new_tree.insert(1, new_tree.root)
		new_tree.insert(2, new_tree.root)
		new_tree.insert(3, new_tree.root)
		new_tree.insert(4, new_tree.root)
		new_tree.insert(5, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-1, 0, 1, 2, 3, 4, 5],
		'insertion failed, tree does not match')
		new_tree.insert(6, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-1, 0, 1, 2, 3, 4, 5, 6],
		'insertion failed, tree does not match')
		self.assertEqual(new_tree.root.data, 2, 'wrong root data')
		self.assertEqual(new_tree.root.color, 'black', 'wrong root color')
		self.assertEqual(new_tree.root.left.data, 0, 'wrong node data')
		self.assertEqual(new_tree.root.left.color, 'red', 'wrong node color')
		self.assertEqual(new_tree.root.right.data, 4, 'wrong node data')
		self.assertEqual(new_tree.root.right.color, 'red', 'wrong node color')
		self.assertEqual(new_tree.root.left.left.data, -1, 'wrong leaf data')
		self.assertEqual(new_tree.root.left.left.color, 'black', 'wrong leaf color')
		self.assertEqual(new_tree.root.left.right.data, 1, 'wrong leaf data')
		self.assertEqual(new_tree.root.left.right.color, 'black', 'wrong leaf color')
		self.assertEqual(new_tree.root.right.left.data, 3, 'wrong leaf data')
		self.assertEqual(new_tree.root.right.left.color, 'black', 'wrong leaf color')
		self.assertEqual(new_tree.root.right.right.data, 5, 'wrong node data')
		self.assertEqual(new_tree.root.right.right.color, 'black', 'wrong node color')
		self.assertEqual(new_tree.root.right.right.right.data, 6, 'wrong leaf data')
		self.assertEqual(new_tree.root.right.right.right.color, 'red', 'wrong leaf color')

	def test_right_left_insertion(self):
		'''
						0																0 (B)											 0(B)												0(B)
					 / \ 														/   \ 											/  \ 											/     \ 
					-1  1													 -1(B) 2 (B)							 -1(B)  2										-1(B)    2
						   \           ->									/  \         -> 					 /  \      ->									/  \ 
								2														 1    3 									 1(B) 3(B)									0.5(B)  3(B)
								 \ 																										 /    											 /  \    
								  3																										0.5        								 0.25  1

						0(B)	 												 0(B)          								0(B)       																	 0.5(B)
					 /   \ 													/   \ 											/     \ 																		 /       \ 
				 -1(B)  2											  -1(B)  2										-1(B)   0.5																	  0         2
				       /  \ 												 /   \ 													/   \ 															/	 \	     /  \ 
						0.5(B) 3(B)				->     				0.5  3(B) -> 								0.25(B)   2								->				-1(B) 0.25(B) 1(B) 3(B)
						/  \ 													 /  \ 																/  \ 																			  \ 
					0.25  1											 0.25(B) 1(B)													 1(B)   3(B)																 	  1.5
								 \ 															 \ 															\ 
								 1.5														1.5															1.5
		'''
		new_tree = red_black_tree.red_black_tree()
		new_tree.insert(0, new_tree.root)
		new_tree.insert(-1, new_tree.root)
		new_tree.insert(1, new_tree.root)
		new_tree.insert(2, new_tree.root)
		new_tree.insert(3, new_tree.root)
		new_tree.insert(0.5, new_tree.root)
		new_tree.insert(0.25, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-1, 0, 0.25, 0.5, 1, 2, 3], 
		'insertional failed, tree does not match')
		new_tree.insert(1.5, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-1, 0, 0.25, 0.5, 1, 1.5, 2, 3],
		'insertion failed, tree does not match')
		self.assertEqual(new_tree.root.data, 0.5, 'wrong root data')
		self.assertEqual(new_tree.root.color, 'black', 'wrong root color')
		self.assertEqual(new_tree.root.left.data, 0, 'wrong node data')
		self.assertEqual(new_tree.root.left.color, 'red', 'wrong node color')
		self.assertEqual(new_tree.root.right.data, 2, 'wrong node data')
		self.assertEqual(new_tree.root.right.color, 'red', 'wrong node color')
		self.assertEqual(new_tree.root.left.left.data, -1, 'wrong leaf data')
		self.assertEqual(new_tree.root.left.left.color, 'black', 'wrong leaf color')
		self.assertEqual(new_tree.root.left.right.data, 0.25, 'wrong leaf data')
		self.assertEqual(new_tree.root.left.right.color, 'black', 'wrong leaf color')
		self.assertEqual(new_tree.root.right.left.data, 1, 'wrong node data')
		self.assertEqual(new_tree.root.right.left.color, 'black', 'wrong node color')
		self.assertEqual(new_tree.root.right.right.data, 3, 'wrong leaf data')
		self.assertEqual(new_tree.root.right.right.color, 'black', 'wrong leaf color')
		self.assertEqual(new_tree.root.right.left.right.data, 1.5, 'wrong leaf data')
		self.assertEqual(new_tree.root.right.left.right.color, 'red', 'wrong leaf color')
		new_tree.delete(1, new_tree.root)
		self.assertEqual(new_tree.inorder_traversal(new_tree.root, []), [-1, 0, 0.25, 0.5, 1.5, 2, 3])

if __name__ == '__main__':
	unittest.main()