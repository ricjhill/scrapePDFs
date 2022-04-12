import PyPDF2


def text_extractor(p):
    data = []
    with open(p, mode='rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        num_pages = reader.getNumPages()
        for i in range(num_pages) :
            page = reader.getPage(i)
            data.append(page.extractText())
    return data


if __name__ == "__main__":
    path = 'sample49.pdf'
    pypdf = text_extractor(path)
    print('The pdf has {} pages and the data structure is a {} where the index refers to the page number.'.format(len(pypdf), type(pypdf)))
    print(pypdf[0])
