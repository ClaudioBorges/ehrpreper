import pandas as pd
from ehrpreper.entity import DocumentEntity


class MimicToRecordConverter:
    def __init__(self):
        pass

    def convert(self, note_events, diagnoses_icd):
        f_ne = self._filterNoteEvents(note_events)
        f_di = self._filterDiagnosesIcd(diagnoses_icd)
        merged = self._merge(f_ne, f_di)
        grouped = (
            merged.groupby(["HADM_ID", "TEXT"])
            .agg(tuple)
            .apply(list)
            .droplevel(level=0)
        )
        return [
            DocumentEntity(text, record["ICD9_CODE"])
            for text, record in grouped.to_dict("index").items()
        ]

    def _filterNoteEvents(self, note_events):
        return note_events[note_events.CATEGORY == "Discharge summary"][
            ["HADM_ID", "TEXT"]
        ]

    def _filterDiagnosesIcd(self, diagnoses_icd):
        return diagnoses_icd[["HADM_ID", "ICD9_CODE"]]

    def _merge(self, note_events, diagnoses_icd):
        return pd.merge(note_events, diagnoses_icd, on="HADM_ID", how="inner")
