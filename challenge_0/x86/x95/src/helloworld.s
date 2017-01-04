.text
.global _start
_start:

        mov     $4,%eax
        mov     $1,%ebx
        mov     $message,%ecx
        mov     $13,%edx
        int 	$0x80

        
        movl    $1,%eax
        movl    $0x0, %ebx
    	int     $0x80

.data

message: 
            .ascii "Hello World!\n"
