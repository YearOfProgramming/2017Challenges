.text
.global _start
_start:
	#example call to function
    	pushq $requestinput
    	pushq $requestbuffer
    	call reverse_string
    	#example output
    	movq $1,%rax
    	movq $1,%rdi
	movq $requestbuffer,%rsi
	movq $5,%rdx
	syscall
	#Exit(0)
    	movq     $60,%rax
    	xorq     %rdi,%rdi
    	syscall

#Function for reversing an input string. Stack contains inputstring as well as a buffer. The caller needs to provide the buffer.
reverse_string:
	#x86 Function Prolog
	pushq %rbp
	movq %rsp, %rbp
	#save registers before smearing them
	pushq %rsi
	pushq %rdi
	pushq %rbx

	#main method
	movq 24(%rbp),%rsi 	#get input string
	movq 16(%rbp),%rdi 	#get output buffer

	push %rsi 		#push input string again for length calculation
	call calc_msglen	#call length calculation
	add $8,%rsp 		#get rid of parameter from string

	add %rax,%rsi 		#move to end of string
	dec %rsi 		#actually we moved one byte too far

	loop:
	movb (%rsi),%bl		#move the char to bl
	movb %bl,(%rdi)		#move the char to output buffer
	dec %rsi 		#move the previous char
	inc %rdi 		#move output buffer pointer forwards
	dec %rax 		#decrease loopsize (msglen)
	test %rax,%rax 		#reached zero?
	jne loop 		#if no -> loop further

	#restoring registers
	popq %rbx
	popq %rdi
	popq %rsi
	#x86 Function Epilog
	movq %rbp , %rsp
	popq %rbp
	ret

#Function for calculating string length
calc_msglen:
	#x86 Function Prolog
	pushq %rbp
	movq %rsp, %rbp
	#save registers before smearing them
	pushq %rcx
	pushq %rdi

	#main method
	xor %rcx, %rcx		#clear rcx
	not %rcx		#set rcx to the highest possible value (rcx will be counting backwards)
	xor %rax, %rax		#clear rax, looking for NULL-Terminator
	cld				#clear direction flag (rdi will move forward one byte)
	movq 16(%rbp),%rdi	#rdi now points to the string
	repne scasb		#looking for NULL-Terminator
	neg %rcx		#negate rcx to get real value
	sub $2, %rcx		#subtract one to compensate negation and one because of the NULL-Termiantor
	mov %rcx,%rax		#x86 convention

	#restore registers
	popq %rdi
	popq %rcx
	#x86 Fuction Epilog
	movq %rbp , %rsp
	popq %rbp
	ret

.data
requestinput: 
            .string "hello"
requestbuffer:
			.space 5
