"""The test file for entity"""

from ehrpreper.entity import DocumentEntity
from ehrpreper.entity import ModelEntity
import pytest


def test_model_entity():
    lang = "lang"
    docs = "docs"
    model = ModelEntity(lang, docs)
    assert model.language == lang
    assert model.documents == docs


def test_document_entity():
    content = "content"
    annotations = "annotations"
    doc = DocumentEntity(content, annotations)
    assert doc.content == content
    assert doc.annotations == annotations
