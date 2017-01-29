import random

class Node(object):
	def __init__(self, data=None, next=None, random=None):
		self.data = data
		self.next = next
		self.random = random

	def __str__(self):
		return("{}".format(self.data))

class LinkedList(object):
	def __init__(self, value):
		if isinstance(value, Node):
			self.root = value
		else:
			self.root = Node(value)

		self.depth = self._calc_depth()
		self.tail = self.root

	def _calc_depth(self):
		node = self.root
		depth = 0

		while node != None:
			depth += 1
			node = node.next

		return(depth)

	def append(self, value):
		self.tail.next = Node(value)
		self.tail = self.tail.next
		self.depth += 1

	def insert(self, node, value):
		new_node = Node(value)
		new_node.next = node.next
		node.next = new_node

	def get_random_node(self):
		node = self.root
		rand_node_id = random.randint(0, self.depth-1)
		
		while rand_node_id > 0:
			node = node.next
			rand_node_id -= 1

		return(node)

	def assign_random_node(self, node):
		if not node:
			return

		# Traverse the linked list to set a value for each node.
		self.assign_random_node(node.next)

		rand_node = node
		# Set the random pointer for the current node
		while rand_node == node:
			rand_node = self.get_random_node()

		node.random = rand_node

	def assign_random_pointers(self):
		self.assign_random_node(self.root)

	# Create a deep copy of this linked list in O(N) time
	def deep_copy(self):
		# Step 1: Copy the linked list by inserting the cloned nodes after the original nodes
		node = self.root
		while node != None:
			self.insert(node, "{}'".format(node.data))
			# Skip the cloned node
			node = node.next.next

		# Step 2: Assign the random links
		node = self.root
		while node != None:
			# node.next is the copy of node, and node.random.next is the copy of node.random
			node.next.random = node.random.next
			# Skip the cloned node
			node = node.next.next

		# Step 3: Restore the original list, and extract the cloned list
		node = self.root
		copy_root = self.root.next
		copy = copy_root
		while node != None:
			node.next = node.next.next
			if copy.next != None:
				copy.next = copy.next.next
			node = node.next
			copy = copy.next

		return(LinkedList(copy_root))

	def print_list(self):
		node = self.root
		while node != None:
			print("{}[{}]".format(node, node.random), end="")
			node = node.next

			if node != None:
				print(" -> ", end="")

		print("\n")

if __name__ == "__main__":
	l1 = LinkedList(1)
	for x in range(2, 10):
		l1.append(x)

	l1.assign_random_pointers()

	l2 = l1.deep_copy()
	l1.print_list()
	l2.print_list()


