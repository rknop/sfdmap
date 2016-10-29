#!/usr/bin/env python
import re
from setuptools import setup

# Synchronize version from code.
version = re.findall(r"__version__ = \"(.*?)\"", open(fname).read())[0]

setup(name="sfdmap",
            version=version,
            description=("Nested sampling algorithms for evaluating "
                                            "Bayesian evidence"),
            long_description="",
            classifiers = ["Development Status :: 4 - Beta",
                           "Programming Language :: Python :: 2",
                           "Programming Language :: Python :: 3",
                           "License :: OSI Approved :: MIT License",
                           "Topic :: Scientific/Engineering",
                           "Topic :: Scientific/Engineering :: Astronomy",
                           "Intended Audience :: Science/Research"],
            py_modules=["sfdmap"],
            url="http://github.com/kbarbary/sfdmap",
            author="Kyle Barbary",
            author_email="kylebarbary@gmail.com")