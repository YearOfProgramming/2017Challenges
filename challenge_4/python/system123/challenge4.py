
class Node:

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


class BinTree:

	def __init__(self):
		self.root = None

	def add(self, value):
		node = Node(value)
		if self.root == None:
			self.root = node
		else:
			self._add(node, self.root)

	def get_root(self):
		return(self.root)

	def invert(self):
		self._swap(self.root)

	def _swap(self, parent):
		if parent == None:
			return

		tmp = parent.right
		parent.right = parent.left
		parent.left = tmp

		self._swap(parent.left)
		self._swap(parent.right)

	def _add(self, node, parent):
		if node.value == None:
			return
		elif node.value <= parent.value:
			if parent.left == None:
				parent.left = node
			else:
				self._add(node, parent.left)
		else:
			if parent.right == None:
				parent.right = node
			else:
				self._add(node, parent.right)

tree = BinTree()
tree.add(4)
tree.add(2)
tree.add(1)
tree.add(3)
tree.add(7)
tree.add(6)
tree.add(9)

print(tree.get_root().left.right.value)
tree.invert()
print(tree.get_root().left.right.value)


