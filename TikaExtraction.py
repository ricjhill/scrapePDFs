from bs4 import BeautifulSoup
from tika import parser
import re
from collections import namedtuple


def text_extractor(filename) -> tuple:
    """
    Tika  lib parses the content from pdf such as
    https://www.op-kzp.sk/wp-content/uploads/2017/09/000_28.vyzva_infoaktivity_v-zneni-informacie.pdf to extract
    the table data  from the  fields  "typ", "operacnyprogram"  and "fond". This is return as a named tuple.
    It is expected that  this  will be  part  of  a  PDF pipeline.

      :param filename: Buffer value
      :return result:  named tuple
    """
    result = namedtuple("Vyzva", ["typ", "operacnyprogram", "fond"])

    def clean_text(text) -> str:
        """
          Parses the string (from pdf )to remove newline spaces, <p> html tags
          :param text: unicode text
          :return res: cleaned string
        """

        res_ob = xhtml_data.find_all("p", string=re.compile(text))
        text = text[1:]
        loc = str(res_ob).rfind(text)
        sentence = re.sub(r"\n+", "", str(res_ob), flags=re.UNICODE)
        res = str(sentence)[loc:].replace("</p>]", "")
        return res

    # Read PDF file
    data = parser.from_file(filename, xmlContent=True)
    xhtml_data = BeautifulSoup(data['content'], 'html.parser')
    result.operacnyprogram = clean_text("^Operačný program")
    result.typ = clean_text("^Typ výzvy")
    result.fond = clean_text("^Fond")

    return result


if __name__ == "__main__":
    path = 'sample28.pdf'
    pypdf = text_extractor(path)

    print(pypdf.typ)
    print(pypdf.operacnyprogram)
    print(pypdf.fond)

