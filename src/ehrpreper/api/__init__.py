"""Elements which wrap the ehrpreper core library for public use."""

from ehrpreper.core import DocumentEntity
from ehrpreper.core import ModelEntity
import lxml.etree as E


def load(path, batch_size=1):
    """Load an ehrpreper_file in batches"""
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


def model_data_generator(model):
    """Content and Annotation (date) based generator for EhrPreper ModelEntity"""
    for document in model.documents:
        yield document.content
        for annotation in document.annotations:
            yield annotation


def data_generator(*ehrpreper_files):
    """Content and Annotation (date) based generator for ehrpreper_files"""
    for ehrpreper_file in ehrpreper_files:
        for model in load(ehrpreper_file):
            for data in model_data_generator(model):
                yield data
