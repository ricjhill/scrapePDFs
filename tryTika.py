from io import StringIO
from bs4 import BeautifulSoup
from tika import parser


def text_extractor(filename):
    data = []
    pages_txt = []

    # Read PDF file
    data = parser.from_file(filename, xmlContent=True)
    xhtml_data = BeautifulSoup(data['content'])
    for i, content in enumerate(xhtml_data.find_all('div', attrs={'class': 'page'})):
        # Parse PDF data using TIKA (xml/html)
        # It's faster and safer to create a new buffer than truncating it
        # https://stackoverflow.com/questions/4330812/how-do-i-clear-a-stringio-object
        _buffer = StringIO()
        _buffer.write(str(content))
        parsed_content = parser.from_buffer(_buffer.getvalue())

        # Add pages
        text = parsed_content['content'].strip()
        pages_txt.append(text)

    return pages_txt


if __name__ == "__main__":
    path = 'sample49.pdf'
    pypdf = text_extractor(path)
    print('The pdf has {} pages and the data structure is a {} where the index refers to the page number.'.format(len(pypdf), type(pypdf)))
    print(pypdf[1])
