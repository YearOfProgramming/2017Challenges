from listNode import listNode


def solution(head):
	lop = dict()
	newHead = listNode()
	temp = head
	temp2 = newHead
	# copy the list first
	while temp != None:
		temp2.val = temp.val
		lop[temp2.val] = temp2
		temp2.next = listNode()
		temp2 = temp2.next
		temp = temp.next
	# assign the random pointers next
	temp3 = head
	temp4 = newHead
	while temp3 != None:
		temp4.random = lop[temp3.random.val]
		temp4 = temp4.next
		temp3 = temp3.next
	return newHead
