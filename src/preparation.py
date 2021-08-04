from argparse import ArgumentParser
from argparse import RawTextHelpFormatter
from processor.xml import XmlProcessor
import config


def make_parser():
    parser = ArgumentParser(
        description="Prepare and normalize a text classification dataset",
        formatter_class=RawTextHelpFormatter,
    )
    parser.add_argument(
        "-i",
        "--input-path",
        default="../input-data",
        help='the input dataset path (default: "../input-data")\n'
        f"        {config.DATASET_MIMIC_III}: DIAGNOSES_ICD.csv and NOTEEVENTS.csv",
    )
    parser.add_argument(
        "-0",
        "--output-file",
        default="../output-data/output.xml",
        help=r'the prepared xml file (default: "../output-data/output.xml")',
    )
    parser.add_argument("dataset", choices=config.DATASETS, help="the dataset type")
    return parser


def main():
    parser = make_parser()
    args = parser.parse_args()
    processor = XmlProcessor()
    processor.process(args.dataset, args.input_path, args.output_file)


if __name__ == "__main__":
    main()
