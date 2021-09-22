"""The test file for entity"""

from ehrpreper.core import DocumentEntity
from ehrpreper.core import ModelEntity


def test_model_entity():
    lang = "lang"
    docs = "docs"
    model = ModelEntity(lang, len(docs), docs)
    assert model.language == lang
    assert model.documents == docs


def test_document_entity():
    content = "content"
    annotations = "annotations"
    doc = DocumentEntity(content, annotations)
    assert doc.content == content
    assert doc.annotations == annotations
