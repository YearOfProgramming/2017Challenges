.text
.global invertTree

invertTree:
	#x86 Prolog
	pushq %rbp
	movq %rsp, %rbp

	# %rdi is input according to AMD64
	xorq %rsi,%rsi 	# %rsi is used to read/write nodes from memory
	xorq %r8,%r8	# %r8 saves the address of the right node
	xorq %r9,%r9	# %r9 saves the address of the left node

	# Get the right node
	movq %rdi,%rsi
	add $8, %rsi
	movq (%rsi),%rsi

	# Traverse right node first
	cmp $0,%rsi
	je skip_right
	pushq %rdi	# Preserve %rdi and proceed with %rsi
	movq %rsi,%rdi
	call invertTree
	popq %rdi
	skip_right:

	# Get the left node
	movq %rdi,%rsi
	add $16, %rsi
	movq (%rsi),%rsi

	# Traverse left node
	cmp $0,%rsi
	je skip_left
	pushq %rdi	# Preserve %rdi and proceed with %rsi
	movq %rsi,%rdi
	call invertTree
	popq %rdi
	skip_left:

	# Get addresses of both nodes
	movq %rdi,%r8
	add $8,%r8
	movq %r8,%r9
	add $8,%r9
	movq (%r8),%r8
	movq (%r9),%r9
	xchgq %r8,%r9	# Switch %r8,%r9

	# Write Back
	movq %rdi,%rsi
	add $8,%rsi
	movq %r8,(%rsi)
	add $8,%rsi
	movq %r9,(%rsi) 


	#x86 Epilog
	movq %rbp , %rsp
	popq %rbp
	ret
