.text
.global check_brackets

check_brackets:
	#x86 Prolog
	pushq %rbp
	movq %rsp, %rbp

	#%rdi input
	#Get ready for some jumpy action... sorry

	#clear registers
	xorq %rax,%rax
	xorq %r8,%r8
	xorq %r9,%r9
	xorq %r10,%r10

	#main method
	stringloop:
	movb (%rdi),%al	#get the current character, abort if NULL-Terminator
	test %al,%al
	je skiploop

	#check for ()
	cmp $40,%al
	jne skip_open_round
	inc %r8
	skip_open_round:

	cmp $41,%al
	jne skip_close_round
	dec %r8
	test %r8,%r8 	#)( is not allowed
	js return_false
	skip_close_round:

	#check for []
	cmp $91,%al
	jne skip_open_rect
	inc %r9
	skip_open_rect:

	cmp $93,%al
	jne skip_close_rect
	dec %r9
	test %r9,%r9 	#][ is not allowed
	js return_false
	skip_close_rect:

	#check for {}
	cmp $123,%al
	jne skip_open_fancy
	inc %r10
	skip_open_fancy:

	cmp $125,%al
	jne skip_close_fancy
	dec %r10
	test %r10,%r10 	#}{ is not allowed
	js return_false
	skip_close_fancy:

	inc %rdi	#move to next char
	jmp stringloop

	skiploop:

	#clear register once again
	xorq %rax,%rax

	#add all counters
	add %r8,%rax
	add %r9,%rax
	add %r10,%rax

	#if Addition >0, not everything is closed
	test %rax,%rax
	je return_true

	return_false:
	xorq %rax,%rax
	jmp epilog

	return_true:
	inc %rax

	epilog:
	#x86 Epilog
	movq %rbp , %rsp
	popq %rbp
	ret
