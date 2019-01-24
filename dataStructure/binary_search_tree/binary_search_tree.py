class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        # prevent duplicate node
        self.count = None


class binary_search_tree:
    def __init__(self):
        self.root = None

    def add(self, data, cur_node):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        elif cur_node is None:
            return new_node
        elif cur_node.data == data:
            cur_node.count = cur_node.count + 1
        elif data < cur_node.data:
            cur_node.left = self.add(data, cur_node.left)
        elif data > cur_node.data:
            cur_node.right = self.add(data, cur_node.right)
        return cur_node

    def delete(self, data, cur_node):
        if self.root is None:
            print('this is an empty tree, impossible to delete')
            return
        elif self.root.left is None and self.root.right is None:
            self.root = None
            return
        elif cur_node is None:
            return None
        elif cur_node.data != data:
            cur_node.left = self.delete(data, cur_node.left)
            cur_node.right = self.delete(data, cur_node.right)
            return cur_node
        else:
            if cur_node.left is None:
                return cur_node.right
            elif cur_node.right is None:
                return cur_node.left
            else:
                # get min value node from right side
                temp_node = self.get_min_child(cur_node.right)
                # assign the min data and count to current node
                cur_node.data = temp_node.data
                cur_node.count = temp_node.count
                # delete the right side min node
                cur_node.right = self.delete(temp_node.data, cur_node.right)
                return cur_node

    def get_min_child(self, cur_node):
        while cur_node.left is not None:
            cur_node = cur_node.left
        return cur_node

    def get_max_child(self, cur_node):
        while cur_node.right is not None:
            cur_node = cur_node.right
        return cur_node

    def find_node(self, data, cur_node):
        if self.root is None:
            print('this is an empty tree, unable to search')
            return None
        elif cur_node is None:
            return None
        elif cur_node.data == data:
            return cur_node
        else:
            '''
            note: None or None -> None
            None or int -> int
            None or str -> str
            None or anything not None -> anything not None
            '''
            return self.find_node(data, cur_node.left) or self.find_node(data, cur_node.right)

    def find_presuc_suc(self, data, cur_node, pre_suc=None, suc=None):
        if self.root is None:
            print('this is an empty tree, no data is found')
        elif cur_node is None:
            return
        elif cur_node.data == data:
            if cur_node.right is not None:
                suc = self.get_min_child(cur_node.right)
            if cur_node.left is not None:
                pre_suc = self.get_max_child(cur_node.left)
        elif cur_node.data > data:
            suc = cur_node
            self.find_presuc_suc(data, cur_node.left)
        elif cur_node.data < data:
            pre_suc = cur_node
            self.find_presuc_suc(data, cur_node.right)
        return pre_suc, suc

    # start will be smaller than the end, assume both two points exist in the tree
    def find_path(self, start, end, cur_node, path=[]):
        if self.root is None:
            print('tree is empty, unable to process')
            return
        if cur_node is None:
            return path
        elif cur_node.data > end:
            path = self.find_path(start, end, cur_node.left, path)
        elif cur_node.data < start:
            path = self.find_path(start, end, cur_node.right, path)
        elif cur_node.data == start:
            if self.find_node(end, cur_node):
                while cur_node.data is not end:
                    path.append(cur_node.data)
                    if cur_node.data < end:
                        cur_node = cur_node.right
                    else:
                        cur_node = cur_node.left
            path.append(cur_node.data)

        elif cur_node.data == end:
            if self.find_node(start, cur_node):
                while cur_node.data is not start:
                    path.insert(0, cur_node.data)
                    if cur_node.data < start:
                        cur_node = cur_node.right
                    else:
                        cur_node = cur_node.left
            path.insert(0, cur_node.data)

        else:
            left_node = right_node = cur_node
            while left_node.data is not start:
                path.insert(0, left_node.data)
                if left_node.data > start:
                    left_node = left_node.left
                else:
                    left_node = left_node.right
            path.insert(0, left_node.data)
            while right_node.data is not end:
                if right_node.data > end:
                    right_node = right_node.left
                else:
                    right_node = right_node.right
                path.append(right_node.data)
        return path


new_tree = binary_search_tree()
new_tree.add(1, new_tree.root)
new_tree.add(3, new_tree.root)
print(new_tree.root.right.data)
new_tree.add(2, new_tree.root)
print(new_tree.root.right.left.data)
new_tree.add(4, new_tree.root)
print(new_tree.root.right.right.data)
new_tree.add(-1, new_tree.root)
print(new_tree.root.data)
print(new_tree.root.right.data)
print(new_tree.root.left.data)
new_tree.delete(1, new_tree.root)
print(new_tree.root.data)
print(new_tree.root.right.data)
print(new_tree.root.right.left)
print(new_tree.root.right.right.data)

new_tree = binary_search_tree()
new_tree.add(1, new_tree.root)
new_tree.add(-1, new_tree.root)
new_tree.add(2, new_tree.root)
print(new_tree.find_presuc_suc(-2, new_tree.root))

'''
		1
	      /   \
	     -1     3
	    / \   /  \
	  -2   0  2   4
	 /  \        / \
	-3   -1.5   3.5 5
'''
new_tree = binary_search_tree()
new_tree.add(1, new_tree.root)
new_tree.add(-1, new_tree.root)
new_tree.add(3, new_tree.root)
new_tree.add(-2, new_tree.root)
new_tree.add(0, new_tree.root)
new_tree.add(-3, new_tree.root)
new_tree.add(-1.5, new_tree.root)
new_tree.add(2, new_tree.root)
new_tree.add(4, new_tree.root)
new_tree.add(3.5, new_tree.root)
new_tree.add(5, new_tree.root)
print(new_tree.find_path(-3, -1, new_tree.root, []))
print(new_tree.find_path(-1.5, -1, new_tree.root, []))
print(new_tree.find_path(-2, 4, new_tree.root, []))
print(new_tree.find_path(0, 2, new_tree.root, []))
