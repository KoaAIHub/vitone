import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="vitone",
    version="1.0",
    description="Format Vietnamese tone",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/KoaAIHub/vitone",
    author="Koa",
    author_email="koadiy.95@gmail.com",
    license="Apache License",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["vitone"],
    include_package_data=True,
    install_requires=["ftfy==5.5.1", "bogo==1.1"],
    entry_points={
        "console_scripts": [
            "realpython=vitone.__main__:main",
        ]
    },
)
