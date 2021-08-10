import logging
import lxml


class XmlWriter:
    def __init__(self):
        pass

    def write(self, xml, output_file):
        logging.info(
            f"{self.__class__.__name__} writing (output_file={output_file})..."
        )
        with open(output_file, "wb") as f:
            content = lxml.etree.tostring(
                xml,
                pretty_print=True,
                xml_declaration=True,
                encoding="UTF-8",
            )
            f.write(content)
