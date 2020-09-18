import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "pycryptometer",
    version = "1.0.0",
    license = "MIT",
    author = "ToasterUwU",
    description = "API Wrapper for cryptometer.io",
    long_description = long_description,
    url = "https://github.com/ToasterUwU/pycryptometer",
    packages = setuptools.find_packages(),
    keywords = ['API', 'Cryptometer'],
    install_requires=[
        'requests',
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: MIT License"
    ],
    python_requires='>=3.6'
)