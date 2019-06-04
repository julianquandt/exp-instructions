import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="exp-instructions",
    version="0.0.1",
    author="Julian Quandt",
    author_email="julian_quandt@live.de",
    description="A convenient way to display experimental instructions in python (via pygame or psychopy).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/julianquandt/exp-instructions",
    #include_package_data = True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)