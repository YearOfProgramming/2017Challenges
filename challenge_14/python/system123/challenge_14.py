
class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.root = None
		self.tail = None

	def _make(self, input_str):
		for c in list(input_str):
			self.add(c)

	def add(self, data):
		if self.root is None:
			self.root = Node(data)
			self.tail = self.root
		else:
			self.tail.next = Node(data)
			self.tail = self.tail.next

	def reverse(self):
		prev = None
		current = self.root
		self.tail = self.root
		
		while current:
			tmp = current.next
			current.next = prev
			prev = current
			current = tmp

		self.root = prev

		return(self)

	def print_list(self):
		x = self.root

		while x:
			print("{}".format(x.data), end=" ")
			x = x.next

		print("\n")

if __name__ == "__main__":
	l = LinkedList()
	l._make(input("Enter your space seperated values to create a LinkedList from: "))
	l.print_list()
	l.reverse()
	l.print_list()

