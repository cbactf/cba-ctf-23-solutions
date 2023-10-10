Set the local variable to 0 in order to bypass the check
```
break *(0x80493ab)
set *(int*)($ebp-0xc) = 0
c
```
