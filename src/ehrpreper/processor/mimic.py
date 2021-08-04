from ehrpreper.converter.mimic import MimicToRecordConverter
from ehrpreper.repository.mimic import MimicRepository


class MimicProcessor:
    def __init__(self):
        self.converter = MimicToRecordConverter()

    def process(self, input_path):
        repo = MimicRepository(input_path)
        diagnoses_icd = repo.find_diagnoses_icd()
        note_events = repo.find_note_events()
        return self.converter.convert(note_events, diagnoses_icd)
