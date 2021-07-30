import pdb

# pdb.set_trace()


from entity.record import DocumentEntity
from entity.record import ModelEntity
from converter.xml import DocumentToXmlConverter
from converter.xml import ModelToXmlConverter
from lxml.etree import tostring

documents = [
    DocumentEntity(content="C1", annotations=[f"A {i}" for i in range(10)]),
    DocumentEntity(content="C2", annotations=[f"B {i}" for i in range(10)]),
    DocumentEntity(content="C3", annotations=[f"C {i}" for i in range(10)]),
]
model = ModelEntity(language="L1", documents=documents)
xml = ModelToXmlConverter().convert(model)

print(
    tostring(
        xml,
        pretty_print=True,
        xml_declaration=True,
        encoding="UTF-8",
    )
)


from repository.mimic import MimicRepository

# repo = MimicRepository("~/master/preparation/input-data")
# df = repo.find_diagnoses_icd()
