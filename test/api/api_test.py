"""The test file for api"""

from ehrpreper.api import load
from ehrpreper.core import DocumentEntity
from ehrpreper.core import ModelEntity


DOCUMENT_MODEL_1 = DocumentEntity("c1", ("c1_a1", "c1_a2"))
DOCUMENT_MODEL_2 = DocumentEntity("c2", ("c2_a1",))
DOCUMENT_MODEL_3 = DocumentEntity("c3", ("c3_a1", "c3_a2", "c3_a3"))
LANGUAGE = "en-US"
MOCKED_DOCUMENT_PATH = "test-data/ehrprepered.xml"


def _load_and_assert(batch_size, docs_batched):
    for model, documents in zip(
        load(MOCKED_DOCUMENT_PATH, batch_size=batch_size), docs_batched
    ):
        assert model == ModelEntity(LANGUAGE, documents)


def test_load_non_batched():
    documents = [(DOCUMENT_MODEL_1,), (DOCUMENT_MODEL_2,), (DOCUMENT_MODEL_3,)]
    _load_and_assert(1, documents)


def test_load_aligned_batch():
    documents = [(DOCUMENT_MODEL_1, DOCUMENT_MODEL_2, DOCUMENT_MODEL_3)]
    _load_and_assert(3, documents)


def test_load_non_aligned_batch():
    documents = [(DOCUMENT_MODEL_1, DOCUMENT_MODEL_2), (DOCUMENT_MODEL_3,)]
    _load_and_assert(2, documents)
