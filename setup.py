import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyjbd-datalux",
    version="0.0.1",
    author="Giuseppe Criscione",
    author_email="giuseppe.criscione@gmail.com",
    description="A Python JSON Based Database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Datalux/pyjbd",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
