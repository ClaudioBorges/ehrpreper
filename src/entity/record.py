import collections

ModelEntity = collections.namedtuple("ModelEntity", ["language", "documents"])

DocumentEntity = collections.namedtuple("DocumentEntity", ["content", "annotations"])
