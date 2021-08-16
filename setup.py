#!/usr/bin/env python

"""The script for setting up ehrpreper."""


import sys

if sys.version_info[0] < 3:
    raise Exception("Ehrpreper does not support Python 2. Please upgrade to Python 3.")

import configparser
from os.path import dirname
from os.path import join

from setuptools import find_packages, setup

# Get the global config info as currently stated
# (we use the config file to avoid actually loading any python here)
config = configparser.ConfigParser()
config.read(["src/ehrpreper/config.ini"])
version = config.get("ehrpreper", "version")


def read(*names, **kwargs):
    """Read a file and return the contents as a string."""
    return open(
        join(dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")
    ).read()


setup(
    name="ehrpreper",
    version=version,
    license="Apache License 2.0",
    description="EHR preparator for ML",
    long_description=read("README.md"),
    # Make sure pypi is expecting markdown!
    long_description_content_type="text/markdown",
    author="Claudio Borges",
    author_email="claudio.borges.jr@gmail.com",
    python_requires=">=3.6",
    keywords=["ehrpreper", "ehr", "ml"],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        # Core
        "configparser",
        "lxml>=4.6.3",
        "pandas>=1.2.5",
    ],
    entry_points={
        "console_scripts": [
            "ehrpreper = ehrpreper.cli:cli",
        ],
    },
)
