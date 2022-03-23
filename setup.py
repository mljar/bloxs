from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="bloxs",
    version="0.0.3",
    description="Display data in an attractive way",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mljar/bloxs",
    author="MLJAR, Sp. z o.o.",
    author_email="contact@mljar.com",
    license="Apache License 2.0",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=open("requirements.txt").readlines(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
    ],
    keywords=[
        "data science",
        "jupyter notebook",
        "data analytics",
        "dashboard",
        "mljar",
    ],
)
