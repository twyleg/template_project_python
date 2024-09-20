# Copyright (C) 2024 twyleg
import versioneer
from pathlib import Path
from setuptools import find_packages, setup


def read(relative_filepath):
    return open(Path(__file__).parent / relative_filepath).read()


def read_long_description() -> str:
    return read("README.md")


# fmt: off
setup(
    name="template_project_python",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Torsten Wylegala",
    author_email="mail@twyleg.de",
    description="",
    license="GPL 3.0",
    keywords="",
    url="https://github.com/twyleg/template_project_python",
    packages=find_packages(),
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[
        "simple-python-app-qt==0.0.1"
    ],
    entry_points={
        "console_scripts": [
            "template_project_python = template_project_python.main:main",
        ]
    },
)
