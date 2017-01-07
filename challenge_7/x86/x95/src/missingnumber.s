.text
.global _start
_start:
	#example call
	pushq $arr
	pushq $10
	call find_missnumber
	#Exit(0)
	#SET BREAKPOINT TO 10 TO SEE RESULT (info registers rax)
    movq     $60,%rax
    xorq     %rdi,%rdi
    syscall

#Function to find the missing number. Callers needs to provide the integer (32-Bit per int) array and the array-size
find_missnumber:
	#x86 Prolog
	pushq %rbp
	movq %rsp, %rbp

	#save registers before smearing
	pushq %rbx
	pushq %rcx
	pushq %rsi

	#main method
	#Get the size of the array, get the address of the array
	movq 16(%rbp),%rax
	movq %rax, %rbx
	movq 24(%rbp),%rsi

	#calculate gauß: sum from 1 to n == n(n+1)/2
	mul %rax
	add %rbx,%rax
	movq $2,%rcx
	div %rcx

	xor %rcx,%rcx	#zero out rcx
	addloop:		#add all numbers in arr to ecx
	add (%rsi),%ecx
	add $4,%rsi
	dec %rbx
	test %rbx,%rbx
	jne addloop

	sub %rcx,%rax	#the missing number is gauß-(sum of arr)

	#restore registers
	popq %rsi
	popq %rcx
	popq %rbx

	#x86 Epilog
	movq %rbp , %rsp
	popq %rbp
	ret

.data
arr: 
	#4 is missing
	.int 9,7,6,1,5,10,8,2,3,0
