from argparse import ArgumentParser
from argparse import RawTextHelpFormatter
from ehrpreper.core.config import *
from ehrpreper.core.processor.xml import XmlProcessor
import logging


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
    parser.add_argument(
        "-x",
        "--extract",
        action="store_true",
        help=r"extract before preparing",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help=r"increse output verbosity",
    )
    parser.add_argument(
        "-p",
        "--parts",
        type=int,
        default=1,
        help=r"number of parts. p files are created using the suffix <part_p> (default: 1)",
    )
    parser.add_argument("dataset", choices=DATASETS, help="the dataset type")
    return parser


def set_logging_level(verbose):
    levels = [logging.WARNING, logging.INFO, logging.DEBUG]
    level = levels[min(len(levels) - 1, verbose)]  # capped to number of levels
    logging.basicConfig(level=level, format="%(asctime)s %(levelname)s %(message)s")


def cli():
    parser = make_parser()
    args = parser.parse_args()
    set_logging_level(args.verbose)

    logging.info(
        f"Started (dataset={args.dataset}, input_path={args.input_path},"
        f" output_file={args.output_file})"
    )
    processor = XmlProcessor()
    processor.process(
        args.dataset,
        args.input_path,
        args.output_file,
        args.extract,
        n_parts=args.parts,
    )
    logging.info("Finished")
