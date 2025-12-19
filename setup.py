"""Setup configuration for Python CLI Tools"""

from setuptools import setup, find_packages

setup(
    name="python-cli-tools",
    version="0.1.0",
    description="A collection of practical Python CLI tools",
    author="Łukasz Perek",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
)
