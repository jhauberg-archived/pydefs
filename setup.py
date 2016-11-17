#!/usr/bin/env python
# coding=utf-8

"""
Setup script for pydefs.

https://github.com/jhauberg/pydefs

Copyright 2016 Jacob Hauberg Hansen.
License: MIT (see LICENSE)
"""

import sys
import re

from setuptools import setup


def determine_version_or_exit() -> str:
    """ Determine version identifier or exit the program. """

    if sys.version_info < (3, 5):
        sys.exit('Python 3.5 or newer is required for pydefs')

    with open('pydefs/version.py') as file:
        version_contents = file.read()

        version_pattern = r'^__version__ = [\'"]([^\'"]*)[\'"]'
        version_match = re.search(version_pattern, version_contents, re.M)

        if version_match:
            return version_match.group(1)
        else:
            sys.exit('Version could not be determined')


VERSION_IDENTIFIER = determine_version_or_exit()


setup(
    name='pydefs',
    version=VERSION_IDENTIFIER,
    description='List functions and classes from Python modules',
    long_description=open('README.md').read(),
    url='https://github.com/jhauberg/pydefs',
    download_url='https://github.com/jhauberg/pydefs/archive/master.zip',
    author='Jacob Hauberg Hansen',
    author_email='jacob.hauberg@gmail.com',
    license='MIT',
    packages=['pydefs'],
    include_package_data=True,
    platforms='any',
    install_requires=[
        'docopt==0.6.2'
    ],
    entry_points={
        'console_scripts': [
            'pydefs = pydefs.__main__:main',
        ],
    }
)
