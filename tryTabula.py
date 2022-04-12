from io import StringIO
from bs4 import BeautifulSoup
import tabula


def text_extractor(filename):
    data = []
    pages_txt = []

    # Read PDF file
    data = tabula.read_pdf(filename, multiple_tables=True, pages="2")

    return data


if __name__ == "__main__":
    path = 'sample49.pdf'
    pypdf = text_extractor(path)
    print('The pdf has {} pages and the data structure is a {} where the index refers to the page number.'.format(len(pypdf), type(pypdf)))
    print(pypdf)
