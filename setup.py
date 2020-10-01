from setuptools import setup, find_packages

with open("README.md", "r") as f:
    longd = f.read()

setup(
    name = "pycryptometer",
    version = "1.3.1",
    license = "MIT",
    author = "ToasterUwU",
    author_email="toasterger@gmail.com",
    description = "API Wrapper for cryptometer.io",
    long_description = longd,
    long_description_content_type = "text/markdown",
    url = "https://github.com/ToasterUwU/pycryptometer",
    packages=[
        "pycryptometer"
    ],
    keywords = ['API-Wrapper', 'Cryptometer'],
    install_requires=[
        'requests',
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6'
)