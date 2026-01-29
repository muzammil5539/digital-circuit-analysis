"""
Setup script for Digital Circuit Analysis package
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="digital-circuit-analysis",
    version="1.0.0",
    author="Digital Circuit Analysis Contributors",
    description="A Python tool for analyzing digital circuits and identifying critical paths",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/muzammil5539/digital-circuit-analysis",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
    ],
    python_requires=">=3.8",
    install_requires=[
        "networkx>=2.8.0",
        "numpy>=1.21.0",
        "matplotlib>=3.5.0",
    ],
    entry_points={
        "console_scripts": [
            "circuit-analyze=src.main:main",
        ],
    },
)
