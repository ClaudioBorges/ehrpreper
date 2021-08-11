"""The test file for xml converter"""

from ehrpreper.core import DocumentEntity
from ehrpreper.core import ModelEntity
from ehrpreper.core.converter.xml import DocumentToXmlConverter
from ehrpreper.core.converter.xml import ModelToXmlConverter


def _assert_xml_document(xml, doc):
    assert xml.tag == "Document"
    childrens = xml.getchildren()
    assert len(childrens) == len(doc.annotations) + 1
    assert childrens[0].tag == "Content"
    assert childrens[0].text == doc.content
    for idx, annotation in enumerate(doc.annotations):
        assert childrens[idx + 1].tag == "Annotation"
        assert childrens[idx + 1].text == annotation


def _assert_xml_model(xml, model):
    assert xml.tag == "Model"
    childrens = xml.getchildren()
    assert len(childrens) == len(model.documents) + 1
    assert childrens[0].tag == "Language"
    assert childrens[0].text == model.language
    for idx, document in enumerate(model.documents):
        _assert_xml_document(childrens[idx + 1], document)


def test_document_to_xml_converter():
    doc = DocumentEntity("content", ["a1", "a2", "a3"])
    xml = DocumentToXmlConverter().convert(doc)
    _assert_xml_document(xml, doc)


def test_model_to_xml_converter():
    model = ModelEntity(
        "language,",
        [
            DocumentEntity("c1", ["a1", "a2", "a3"]),
            DocumentEntity("c1", ["a1", "a2", "a3"]),
        ],
    )
    xml = ModelToXmlConverter().convert(model)
    _assert_xml_model(xml, model)
