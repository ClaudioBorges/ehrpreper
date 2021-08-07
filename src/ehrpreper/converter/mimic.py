from ehrpreper.entity import DocumentEntity
import logging
import pandas as pd


class MimicToRecordConverter:
    def __init__(self):
        pass

    def convert(self, note_events, diagnoses_icd):
        logging.info(f"{self.__class__.__name__} converting...")
        f_ne = self._filterNoteEvents(note_events)
        f_di = self._filterDiagnosesIcd(diagnoses_icd)
        merged = self._merge(f_ne, f_di)
        non_na = merged.dropna()
        grouped = (
            non_na.groupby(["HADM_ID", "TEXT"])
            .agg(tuple)
            .apply(list)
            .droplevel(level=0)
        )
        logging.debug(f"Statistic (note_events={len(note_events)})")
        logging.debug(f"Statistic (diagnoses_icd={len(diagnoses_icd)})")
        logging.debug(f"Statistic (filtered_note_events={len(f_ne)})")
        logging.debug(f"Statistic (filtered_diagnoses_icd={len(f_di)})")
        logging.debug(f"Statistic (merged={len(merged)})")
        logging.debug(f"Statistic (non_na={len(non_na)})")
        logging.debug(f"Statistic (grouped={len(grouped)})")
        return [
            DocumentEntity(text, record["ICD9_CODE"])
            for text, record in grouped.to_dict("index").items()
        ]

    def _filterNoteEvents(self, note_events):
        logging.debug('Filtering note_events by "Discharge summary"...')
        return note_events[note_events.CATEGORY == "Discharge summary"][
            ["HADM_ID", "TEXT"]
        ]

    def _filterDiagnosesIcd(self, diagnoses_icd):
        return diagnoses_icd[["HADM_ID", "ICD9_CODE"]]

    def _merge(self, note_events, diagnoses_icd):
        logging.debug("Merging note events and diagnoses icd (how=inner)")
        return pd.merge(note_events, diagnoses_icd, on="HADM_ID", how="inner")
