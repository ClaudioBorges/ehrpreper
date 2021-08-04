from argparse import ArgumentParser
from argparse import RawTextHelpFormatter
from ehrpreper.config import *
from ehrpreper.processor.xml import XmlProcessor


def make_parser():
    parser = ArgumentParser(
        description="Prepare and normalize a text classification dataset",
        formatter_class=RawTextHelpFormatter,
    )
    parser.add_argument(
        "-i",
        "--input-path",
        default="../data/input",
        help='the input dataset path (default: "../data/input")\n'
        f"        {DATASET_MIMIC_III}: DIAGNOSES_ICD.csv and NOTEEVENTS.csv",
    )
    parser.add_argument(
        "-o",
        "--output-file",
        default="../data/output/output.xml",
        help=r'the prepared xml file (default: "../data/output/output.xml")',
    )
    parser.add_argument("dataset", choices=DATASETS, help="the dataset type")
    return parser


def cli():
    parser = make_parser()
    args = parser.parse_args()
    processor = XmlProcessor()
    processor.process(args.dataset, args.input_path, args.output_file)
