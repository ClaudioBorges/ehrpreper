"""Elements which wrap the ehrpreper core library for public use."""

from ehrpreper.core import DocumentEntity
from ehrpreper.core import ModelEntity
import lxml.etree as E


def load(path, batch_size=1):
    language = None
    documents = ()
    content = None
    annotations = ()

    for _, element in E.iterparse(path):
        if element.tag == "Language":
            language = element.text
        elif element.tag == "Content":
            content = element.text
        elif element.tag == "Annotation":
            annotations += (element.text,)
        elif element.tag == "Document":
            documents += (DocumentEntity(content, annotations),)
            content = None
            annotations = ()
            if len(documents) == batch_size:
                yield ModelEntity(language, documents)
                documents = ()

    if len(documents) > 0:
        yield ModelEntity(language, documents)
