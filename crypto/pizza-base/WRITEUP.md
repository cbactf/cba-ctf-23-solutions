# pizza base

The description should give a hint of what its encoded in (base and rot). The most common is base64 and rot13, but you can have a play around with other variations (base32, rot15 etc) on https://gchq.github.io/CyberChef/.

The string we are given is `TGJoIGZuaXJxIGd1ciBjdm1tbiBvbmZyIHNlYnogdGJ2YXQgYnNzISBVcmVyIHZmIGd1ciBzeW50IFBPTlBHU3tjdjMzbl8xZl9lUm5xbH0=`

It looks like a base64 string, so on cyberchef we can put the "From Base64" first and then we see `Lbh fnirq gur cvmmn onfr sebz tbvat bss! Urer vf gur synt PONPGS{cv33n_1f_eRnql}`. Ooh there are some curly brackets, which might be a flag...

Rot13 is when a character is rotated 13 times, so let's add "ROT13" to the cyberchef recipe.

We get this as the final output: `You saved the pizza base from going off! Here is the flag CBACTF{pi33a_1s_rEady}`

Flag: CBACTF{pi33a_1s_rEady}