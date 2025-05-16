from setuptools import setup, find_packages

setup(
    name="my_awesome_lib",                 
    version="0.1.0",                       
    author="Igor",                   
    description="Biblioteka do obliczeń matematycznych, przetwarzania tekstu i operacji na danych.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
