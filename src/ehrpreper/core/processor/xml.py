from ehrpreper.core.config import DATASET_CONFIG_MAP
from ehrpreper.core.converter.xml import ModelToXmlConverter
from ehrpreper.core.entity import ModelEntity
from ehrpreper.core.writer.xml import XmlWriter
from lxml.etree import tostring
import logging


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

    def process(self, config_key, input_path, output_file, extract):
        logging.info(f"{self.__class__.__name__} processing...")
        cfg = self.config_map[config_key]
        documents = cfg.processor.process(input_path, extract)
        model = ModelEntity(language=cfg.language, documents=documents)
        xml = self.converter.convert(model)
        self.writer.write(xml, output_file)
