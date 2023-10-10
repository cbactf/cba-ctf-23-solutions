## File upload through filter bypass and ssti

Firstly robots.txt reveals the log file /logs/devchat01.log. The log contains a conversation with information about using Jinja templates that may be vulnerable once someone gets past the file type filters.

The only functionality of the website that works is the lodge a complaint form. The text data is not processed by the back end so will be ignored. An evidential image is then required, if a different file format is supplied the server rejects it.

To get a text file (.txt, .php, .html, .py, .md and more) past the first filter a null byte may be used. For example filename "test.txt%00.jpg" will be accepted.

To pass the second filter magic number or file signatures need to be added to the beginning of the file. For example '\xFF\xD8\xFF' for jpg, '\x89\x50\x4E\x47\x0D\x0A\x1A\x0A' for png, or '\x47\x49\x46\x38\x37\x61' for 'gif'. A program such as hexedit can be used for this. 

Then the output of this text file will be reflected in the templated response error message. The template is vulnerable to ssti. An example of file content that will work:

Filename:'test.txt%00.jpg'

Contents: 
b(xFFxD8xFF){% for x in ().__class__.__base__.__subclasses__() %}{% if "warning" in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen("cat flag.txt").read()}}{%endif%}{% endfor %}