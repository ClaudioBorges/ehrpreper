import collections

ModelEntity = collections.namedtuple(
    "ModelEntity", ["language", "num_documents", "documents"]
)
DocumentEntity = collections.namedtuple("DocumentEntity", ["content", "annotations"])
