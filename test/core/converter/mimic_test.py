"""The test file for mimic converter"""

from ehrpreper.core.converter.mimic import MimicToRecordConverter
from ehrpreper.core.entity import DocumentEntity
import pandas as pd


def test_mimic_to_record_converter():
    diagnoses_icd = {"HADM_ID": [1, 1, 2], "ICD9_CODE": [1, 2, 3]}
    note_events = {
        "HADM_ID": [1, 2, 3],
        "CATEGORY": ["Discharge summary", "Discharge summary", "other"],
        "TEXT": ["t1", "t2", "t3"],
    }
    expected_docs = [DocumentEntity("t1", (1, 2)), DocumentEntity("t2", (3,))]

    df_diagnoses_icd = pd.DataFrame(data=diagnoses_icd)
    df_note_events = pd.DataFrame(data=note_events)
    docs = MimicToRecordConverter().convert(df_note_events, df_diagnoses_icd)

    assert len(docs) == len(expected_docs)
    for doc, expected in zip(docs, expected_docs):
        assert doc == expected
