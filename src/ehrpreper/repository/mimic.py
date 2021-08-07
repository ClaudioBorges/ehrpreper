import pandas as pd
import os


class MimicRepository:
    """Mimic Repository"""

    def __init__(self, base_path):
        self.base_path = base_path

    def find_diagnoses_icd(self):
        return pd.read_csv(
            os.path.join(self.base_path, "DIAGNOSES_ICD.csv"), dtype="str"
        )

    def find_note_events(self):
        return pd.read_csv(os.path.join(self.base_path, "NOTEEVENTS.csv"), dtype="str")
