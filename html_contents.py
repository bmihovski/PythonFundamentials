"""
You have been tasked to create a program which represents a Console interface for creating HTML files.
Every HTML file naturally holds the following elements:
"<!DOCTYPE html>
 <html>
 <head>
 </head>
 <body>
 </body>
 </html>"
You will need to add them at the end in order to form the file.
You will start receiving input lines in the following format:
{tag} {content}
You should generate a string from every input line - like this: <{tag}>{content}</{tag}> …
If the tag is "title" you should add the generated string between the <head> and
</head> tags with a tabulation ("\t") before it.
If you receive the "title" tag MORE than ONCE, you should CHANGE its value.
In any other case you should APPEND the generated string between the <body> and
</body> tags with a tabulation ("\t") before it.
When you receive the command "exit" the input ends. The content you have generated should be stored in
a file called "index.html" (.html extension).

Examples

Input
h1 Heading
h2 Heading
h3 Heading
h4 Heading
h5 Heading
h6 Heading
title Test
p 1.Paragraph
p 2.ParagraphTwo
div SimpleDiv
title HTML-Contents
exit

Output
<!DOCTYPE html>
<html>
<head>
   <title>HTML-Contents</title>
</head>
<body>
   <h1>Heading</h1>
   <h2>Heading</h2>
   <h3>Heading</h3>
   <h4>Heading</h4>
   <h5>Heading</h5>
   <h6>Heading</h6>
   <p>1.Paragraph</p>
   <p>2.ParagraphTwo</p>
   <div>SimpleDiv</div>
</body>
</html>
"""


class Title:
    def __init__(self, title):
        """
        Constructs html title tag
        :param title: (Str) Title tag content
        """
        self.title = title

    def gen_title(self):
        """
        Generates tag title in html format
        :return: (Str) Generated title html content
        """
        title = f'\t<title>{self.title}</title>\n'
        return title


class Body:
    def __init__(self, tag, content):
        """
        Constructs html body content
        :param tag: (Str) Tag name
        :param content: (Str) Tag content
        """
        self.tag = tag
        self.content = content

    def gen_body(self):
        """
        Generates body content in html format
        :return: (Str) Generated body html content
        """
        body_elem = f'\t<{self.tag}>{self.content}</{self.tag}>\n'
        return body_elem


input_html_elems = list()
title_content = None
body_contents = list()

while True:
    input_html_elems = input().split()
    if 'exit' in input_html_elems:
        break
    elif 'title' == input_html_elems[0]:
        title_content = Title(input_html_elems[1])
    else:
        body_contents.append(Body(tag=input_html_elems[0], content=input_html_elems[1]))

with open('./index.html', 'w+') as index_file:
    index_file.write('<!DOCTYPE html>\n')
    index_file.write('<html>\n')
    index_file.write('<head>\n')
    index_file.write(f'{title_content.gen_title()}')
    index_file.write(f'</head>\n')
    index_file.write(f'<body>\n')
    [index_file.write(elem.gen_body()) for elem in body_contents]
    index_file.write('</body>\n')
    index_file.write('</html>\n')
