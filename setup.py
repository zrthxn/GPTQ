from setuptools import setup, find_packages
from pathlib import Path

def read_requirements():
    return list(Path("requirements.txt").read_text().splitlines())


setup(
	name = "gptq",
	version = "0.0.3",
	author = "fpgaminer",
	author_email = "fpgaminer@bitcoin-mining.com",
	description = "Fast GPTQ kernels written in Triton",
	license = "Apache License 2.0",
	license_file = "LICENSE",
    packages=find_packages(),
    install_requires=read_requirements(),
)
