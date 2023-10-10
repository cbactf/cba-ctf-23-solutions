# meta

The description and title of the image is a big hint in terms of what to look at. The metadata of a photo includes properties such as the location, author and comments.

There are 2 ways to complete the challenge.

In terminal, we can run `file meta.jpg`. This gives us the flag.

    meta.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 0x0, segment length 16, comment: "CBACTF{ch3ck_METAdata_always!}", baseline, precision 8, 3840x2160, components 3

Using a tool called `exiftool`, in terminal we can run the command `exiftool meta.jpg`

This will list out all the metadata and we see that the flag is hidden in the comment section. This tool is automatically installed on Kali Linux.

flag: CBACTF{ch3ck_METAdata_always!}

