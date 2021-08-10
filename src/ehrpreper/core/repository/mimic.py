import logging
import os
import pandas as pd


class MimicRepository:
    """Mimic Repository"""

    def __init__(self, base_path):
        self.base_path = base_path

    def find_diagnoses_icd(self):
        logging.info(f"{self.__class__.__name__} finding diagnoses icd...")
        return pd.read_csv(
            os.path.join(self.base_path, "DIAGNOSES_ICD.csv"), dtype="str"
        )

    def find_note_events(self):
        logging.info(f"{self.__class__.__name__} finding note events...")
        return pd.read_csv(os.path.join(self.base_path, "NOTEEVENTS.csv"), dtype="str")
