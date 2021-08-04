from lxml.builder import E


class DocumentToXmlConverter:
    def __init__(self):
        pass

    def convert(self, documentEntity):
        xmlContent = self._makeXmlContent(documentEntity.content)
        xmlAnnotations = self._makeXmlAnnotations(documentEntity.annotations)
        return self._makeDocument(xmlContent, xmlAnnotations)

    def _makeDocument(self, xmlContent, xmlAnnotations):
        return E.Document(xmlContent, *xmlAnnotations)

    def _makeXmlContent(self, content):
        return E.Content(content)

    def _makeXmlAnnotations(self, annotations):
        return [E.Annotation(annotation) for annotation in annotations]


class ModelToXmlConverter:
    def __init__(self, documentToXmlConverter=DocumentToXmlConverter()):
        self._documentConverter = documentToXmlConverter

    def convert(self, modelEntity):
        xmlLanguage = self._makeXmlLanguage(modelEntity.language)
        xmlDocuments = self._makeXmlDocuments(modelEntity.documents)
        return self._makeModel(xmlLanguage, xmlDocuments)

    def _makeModel(self, xmlLanguage, xmlDocuments):
        return E.Model(xmlLanguage, *xmlDocuments)

    def _makeXmlLanguage(self, language):
        return E.Language(language)

    def _makeXmlDocuments(self, documents):
        return [self._documentConverter.convert(document) for document in documents]
