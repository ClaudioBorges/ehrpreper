import logging
import os
import pandas as pd


class MimicRepository:
    """Mimic Repository"""

    def __init__(self, base_path, extract):
        self._base_path = base_path
        self._extension = ".csv.gz" if extract else ".csv"

    def find_diagnoses_icd(self):
        logging.info(f"{self.__class__.__name__} finding diagnoses icd...")
        return pd.read_csv(
            os.path.join(self._base_path, f"DIAGNOSES_ICD{self._extension}"),
            dtype="str",
        )

    def find_note_events(self):
        logging.info(f"{self.__class__.__name__} finding note events...")
        return pd.read_csv(
            os.path.join(self._base_path, f"NOTEEVENTS{self._extension}"), dtype="str"
        )
