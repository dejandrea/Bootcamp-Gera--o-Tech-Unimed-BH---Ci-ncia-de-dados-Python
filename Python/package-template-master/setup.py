from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="img_processingg",
    version="0.0.1",
    author="Andréa J S França",
    author_email="dejandrea@gmail.com",
    description="My short description",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dejandrea/Bootcamp-Gera--o-Tech-Unimed-BH---Ci-ncia-de-dados-Python.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.7',
)