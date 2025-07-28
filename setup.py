"""
Setup script for MCP4922 DAC library
"""

from setuptools import setup, find_packages
import os

def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Python Library for driving MCP4922 DAC on Raspberry Pi"

setup(
    name="rpi-mcp4922",
    version="1.0.0",
    author="mrwunderbar666",
    author_email="",
    maintainer="AymericFerreira",
    maintainer_email="aymeric.ferreira@gmail.com",
    description="Python Library for driving MCP4922 DAC on Raspberry Pi",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/mrwunderbar666/Python-RPi-MCP4922",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: System :: Hardware",
        "Topic :: System :: Hardware :: Hardware Drivers",
    ],
    python_requires=">=3.7",
    install_requires=[
        "RPi.GPIO>=0.7.0",
        "spidev>=3.4",
    ],
    extras_require={
        "dev": [
            "pytest",
            "ruff",
        ],
    },
    keywords="raspberry pi, mcp4922, dac, spi, gpio, digital to analog",
    project_urls={
        "Bug Reports": "https://github.com/mrwunderbar666/Python-RPi-MCP4922/issues",
        "Source": "https://github.com/mrwunderbar666/Python-RPi-MCP4922",
    },
)
