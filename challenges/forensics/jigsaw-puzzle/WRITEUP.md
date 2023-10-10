# jigsaw-puzzle

As the description suggests, you have to piece together everything.

## Adelaide.jpg

This one uses `exiftool`, where the author is the string you are looking for. `exiftool Adelaide.jpg`, when you scroll to the author, you will see fgng3f_ which is a rot13 string. Decrypting that gives `stat3s_`

## Brisbane.jpg

Using steghide, you use the command `steghide extract -sf Brisbane.jpg`, which prompts you for a passphrase. This is where the password.txt comes in handy. The clue given in the password.txt is "When our journey began as grads...", followed by "--/-/--". Hopefully you think of the date we started which is 20/2/23, which is the passphrase. Entering that will give you the secret.txt file, which gives `.---- ..--.- ... ...-- ...--`. This is morse code, putting in cyberchef gives you `1_S33`

## Melbourne.jpg

In the sky we see `4342414354467b30746865725f`, you have to work out that this is a hex string. Putting it through cyberchef gives `CBACTF{0ther`

## Perth.pdf.png.zip.jpg

This might be the trickiest to work out. Looking at the hexdump shows that it's a JPEG file due to the hex being JFIF, but we can see the file is corrupt. The first 6 characters of the hex is `35 90 DE`, but a real JPEG hex should be `FF D8 FF`. Using a hexeditor or running `hexedit Perth.pdf.png.zip.jpg` allows you to change the hex. Correcting the hex header gives you the jpg file which should show `_YoU}`

Flag: CBACTF{0ther_stat3s_1_S33_YoU}