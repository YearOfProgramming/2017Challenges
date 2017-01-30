
class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def find_smallest(self):
		if self.left:
			return(self.left.find_smallest())
		else:
			return(self.data)

	def insert(self, data):
		if data < self.data:
			if self.left is None:
				self.left = Node(data)
			else:
				self.left.insert(data)
		else:
			if self.right is None:
				self.right = Node(data)
			else:
				self.right.insert(data)

	def remove(self, data):
		if data < self.data:
			if self.left is not None:
				self.left = self.left.remove(data)
		elif data > self.data:
			if self.right is not None:
				self.right = self.right.remove(data)
		else:
			if self.left is None and self.right is not None:
				return(self.right)
			elif self.left is not None and self.right is None:
				return(self.left)
			elif self.left is None and self.right is None:
				return(None)
				
			self.data = self.right.find_smallest()
			self.right = self.right.remove( self.data )

		return(self)

	def print_tree(self, tabs=0):
		if self.left is not None:
			self.left.print_tree()

		print("{}{}".format('  ' * tabs, str(self.data)))

		if self.right is not None:
			self.right.print_tree()
		

class BinTree(object):
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root is None:
			self.root = Node(data)
		else:
			self.root.insert(data)

	def remove(self, data):
		if self.root is not None:
			self.root.remove(data)

	def print_tree(self):
		if self.root is not None:
			self.root.print_tree()

if __name__ == "__main__":
	btree = BinTree()

	data = list(input("Enter data to insert: "))

	for x in data:
		btree.insert(x)

	btree.print_tree()

	btree.remove( input("Enter a value to delete: ") )

	btree.print_tree()
