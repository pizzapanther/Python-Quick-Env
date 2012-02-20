import sys

from setuptools import setup, find_packages

setup(
    name = "pyquickenv",
    version = '1.0.3',
    description = "A command line tool to start Python virtual environments faster and easier.",
    url = "https://github.com/pizzapanther/Python-Quick-Env",
    author = "Paul Bailey",
    author_email = "paul.m.bailey@gmail.com",
    license = "BSD",
    packages = ['pyquickenv'],
    entry_points = {
        "console_scripts": [
            "pyquickenv = pyquickenv.__main__:main",
        ],
    },
)
