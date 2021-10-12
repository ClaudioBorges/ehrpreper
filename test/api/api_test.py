"""The test file for api"""

import ehrpreper.core as core
import ehrpreper.api as api


DOCUMENT_MODEL_1 = core.DocumentEntity("c1", ("c1_a1", "c1_a2"))
DOCUMENT_MODEL_2 = core.DocumentEntity("c2", ("c2_a1",))
DOCUMENT_MODEL_3 = core.DocumentEntity("c3", ("c3_a1", "c3_a2", "c3_a3"))
DOCUMENTS = (
    DOCUMENT_MODEL_1,
    DOCUMENT_MODEL_2,
    DOCUMENT_MODEL_3,
)
DOCUMENTS_FLAT = (
    "c1",
    "c1_a1",
    "c1_a2",
    "c2",
    "c2_a1",
    "c3",
    "c3_a1",
    "c3_a2",
    "c3_a3",
)
SIZE = 3
LANGUAGE = "en-US"
MOCKED_DOCUMENT_PATH = "test-data/ehrprepered.xml"


def _load_and_assert(batch_size, docs_batched):
    for model, documents in zip(
        api.load(MOCKED_DOCUMENT_PATH, batch_size=batch_size), docs_batched
    ):
        assert model == core.ModelEntity(LANGUAGE, len(documents), documents)


def test_load_non_batched():
    documents = [(DOCUMENT_MODEL_1,), (DOCUMENT_MODEL_2,), (DOCUMENT_MODEL_3,)]
    _load_and_assert(1, documents)


def test_load_aligned_batch():
    documents = [(DOCUMENT_MODEL_1, DOCUMENT_MODEL_2, DOCUMENT_MODEL_3)]
    _load_and_assert(3, documents)


def test_load_non_aligned_batch():
    documents = [(DOCUMENT_MODEL_1, DOCUMENT_MODEL_2), (DOCUMENT_MODEL_3,)]
    _load_and_assert(2, documents)


def test_model_data_generator():
    models = api.load(MOCKED_DOCUMENT_PATH, batch_size=3)
    got = tuple(elm for model in models for elm in api.model_data_generator(model))
    assert got == DOCUMENTS_FLAT


def test_data_generator():
    got = tuple(elm for elm in api.data_generator(MOCKED_DOCUMENT_PATH))
    assert got == DOCUMENTS_FLAT


def test_size():
    got = api.size(MOCKED_DOCUMENT_PATH)
    assert got == SIZE


def test_document_entity_generator():
    got = api.document_entity_generator(MOCKED_DOCUMENT_PATH)
    for document_got, document_expected in zip(got, DOCUMENTS):
        assert document_got == document_expected


def test_convert_icd():
    icd9 = "0031"
    icd10 = "A021"
    converter = api.Icd9To10Converter()
    assert converter.convert(icd9) == icd10
    assert converter.convert("something") == "UNK"
