from listNode import listNode


def solution(head):
	# by keeping track of the pointers rather than their values, we can insure that
	# there a duplicates in the linked list.
	lop = dict()
	newHead = listNode()
	temp = head
	temp2 = newHead
	# copy the list first
	while temp.next != None:
		temp2.val = temp.val
		lop[temp] = temp2
		temp2.next = listNode()
		temp2 = temp2.next
		temp = temp.next
	temp2.next = None
	# assign the random pointers
	temp3 = head
	temp4 = newHead
	while temp3.next != None:
		temp4.random = lop[temp3.random]
		temp3 = temp3.next
		temp4 = temp4.next

	return newHead
