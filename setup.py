# akettunen copyright 2026
# This is just an helper file or something
from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("mindows.py", language_level=3))
