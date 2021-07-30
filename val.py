from lxml import etree

parser = etree.XMLParser(dtd_validation=True)


from lxml.etree import tostring
from lxml.builder import E

print(
    tostring(
        E.results(
            E.Country(
                name="Germany", Code="DE", Storage="Basic", Status="Fresh", Type="Photo"
            )
        ),
        pretty_print=True,
        xml_declaration=True,
        encoding="UTF-8",
    )
)

import pdb

# pdb.set_trace()


def document():
    args = [E.Annotation(str(t)) for t in range(1000)]
    return E.Document(E.Content("Content"), *args)


def model():
    return E.Model(E.Language("en"), document())


print(
    tostring(
        model(),
        pretty_print=True,
        xml_declaration=True,
        encoding="UTF-8",
    )
)


# schema_content = open("learn_input.xsd", "rb").read()
# xml_content = open("learn_input_example.xml", "rb").read()
#
# schema_root = etree.XML(schema_content)
# schema = etree.XMLSchema(schema_root)
#
# parser = etree.XMLParser(schema=schema)
# root = etree.fromstring(xml_content, parser)
