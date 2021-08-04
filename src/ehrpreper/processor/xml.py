from ehrpreper.config import DATASET_CONFIG_MAP
from ehrpreper.converter.xml import ModelToXmlConverter
from ehrpreper.entity import ModelEntity
from ehrpreper.writer.xml import XmlWriter
from lxml.etree import tostring


class XmlProcessor:
    def __init__(
        self,
        config_map=DATASET_CONFIG_MAP,
        writer=XmlWriter(),
        converter=ModelToXmlConverter(),
    ):
        self.config_map = config_map
        self.writer = writer
        self.converter = converter

    def process(self, config_key, input_path, output_file):
        cfg = self.config_map[config_key]
        documents = cfg.processor.process(input_path)
        model = ModelEntity(language=cfg.language, documents=documents)
        xml = self.converter.convert(model)
        self.writer.write(xml, output_file)
