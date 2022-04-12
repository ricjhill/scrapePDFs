from io import StringIO
from bs4 import BeautifulSoup
from tika import parser
import re
from tika import detector
from tika import config

import pandas as pd


def text_extractor(filename):
    data = []
    pages_txt = []

    # Read PDF file
    data = parser.from_file(filename, xmlContent=True)
    xhtml_data = BeautifulSoup(data['content'], 'html.parser')
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

    xhtml_data.find_all('p')
    print(xhtml_data.find_all("p", string=re.compile("^Typ výzvy")))
    print(xhtml_data.find_all("p", string=re.compile("^Operačný program")))
    print(xhtml_data.find_all("p", string=re.compile("^Fond")))

    return pages_txt


def getclosingdate(xhtmlfile)-> str:
    xhtml_soup = BeautifulSoup(xhtmlfile, 'html.parser')
    print(xhtml_soup.prettify())
    print(type(xhtml_soup))
    xhtml_soup.find_all('p')
    re.compile

    return None



#def getstatus(file)-> str:
#
#    return status


if __name__ == "__main__":
    path = 'sample49.pdf'
    pypdf = text_extractor(path)
    print('The pdf has {} pages and the data structure is a {} where the index refers to the page number.'.format(len(pypdf), type(pypdf)))
    #print(pypdf[1])
    #getclosingdate(pypdf[1])
