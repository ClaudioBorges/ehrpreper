from converter.xml import ModelToXmlConverter
from entity import ModelEntity
from lxml.etree import tostring
from writer.xml import XmlWriter
import config


class XmlProcessor:
    def __init__(
        self,
        config_map=config.DATASET_CONFIG_MAP,
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
