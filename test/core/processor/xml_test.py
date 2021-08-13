from ehrpreper.core.config import Config
from ehrpreper.core.entity import ModelEntity
from ehrpreper.core.processor.xml import XmlProcessor
from unittest.mock import Mock


def test_xml_processor():
    converter = Mock()
    documents = Mock()
    processor = Mock()
    writer = Mock()
    xml = Mock()

    converter.convert.return_value = xml
    processor.process.return_value = documents
    config = {"key": Config(processor=processor, language="language")}
    xml_processor = XmlProcessor(config_map=config, writer=writer, converter=converter)
    xml_processor.process("key", "input_path", "output_file", False)

    processor.process.called_once_with("input_path")
    converter.convert.called_once_with(
        ModelEntity(language="language", documents=documents)
    )
    writer.write.called_once_with(xml, "output_file")
