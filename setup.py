from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Presentation parser for LLM",
    version="0.0.1",
    description="Simple json2pptx; sample json is in the /sample subfolder",
    long_description=long_description,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
    install_requires=[
        "python-pptx",
        "pillow",
        "matplotlib",
    ]
)