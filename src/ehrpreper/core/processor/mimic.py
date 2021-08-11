from ehrpreper.core.converter.mimic import MimicToRecordConverter
from ehrpreper.core.repository.mimic import MimicRepository
import logging


class MimicProcessor:
    def __init__(self):
        self._converter = MimicToRecordConverter()

    def process(self, input_path):
        logging.info(f"{self.__class__.__name__} processing...")
        repo = MimicRepository(input_path)
        diagnoses_icd = repo.find_diagnoses_icd()
        note_events = repo.find_note_events()
        return self._converter.convert(note_events, diagnoses_icd)
