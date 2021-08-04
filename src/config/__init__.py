from processor.mimic import MimicProcessor
import collections

Config = collections.namedtuple("Config", ["processor", "language"])

DATASET_MIMIC_III = "mimicIII"
DATASETS = [DATASET_MIMIC_III]

LANGUAGE_EN_US = "en-US"

DATASET_CONFIG_MAP = {
    DATASET_MIMIC_III: Config(processor=MimicProcessor(), language=LANGUAGE_EN_US),
}
