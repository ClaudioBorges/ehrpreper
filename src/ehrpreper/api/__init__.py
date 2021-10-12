"""Elements which wrap the ehrpreper core library for public use."""

from ehrpreper.core import DocumentEntity
from ehrpreper.core import ModelEntity
import lxml.etree as E
import pkg_resources


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
                yield ModelEntity(language, len(documents), documents)
                documents = ()

    if len(documents) > 0:
        yield ModelEntity(language, len(documents), documents)


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


def size(*ehrpreper_files):
    """Number of DocumentEntity"""
    return sum(
        [
            1
            for ehrpreper_file in ehrpreper_files
            for model in load(ehrpreper_file, batch_size=1)
        ]
    )


def document_entity_generator(*ehrpreper_files):
    """Generator of DocumentEntity"""
    return (
        document
        for ehrpreper_file in ehrpreper_files
        for model in load(ehrpreper_file)
        for document in model.documents
    )


class Icd9To10Converter:
    ICD_9_10_MAP = None

    def __init__(self):
        if Icd9To10Converter.ICD_9_10_MAP is None:
            map_file = pkg_resources.resource_filename("ehrpreper", "2018_I9gem.txt")
            with open(map_file) as file:
                Icd9To10Converter.ICD_9_10_MAP = {
                    self._line_to_icd9(line): self._line_to_icd10(line) for line in file
                }

    def _line_to_icd9(self, line):
        return line[:6].strip()

    def _line_to_icd10(self, line):
        return line[6:14].strip()

    def convert(self, icd9, default="UNK"):
        return Icd9To10Converter.ICD_9_10_MAP.get(icd9, default)
