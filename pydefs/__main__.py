#!/usr/bin/env python
# coding=utf-8

"""
List functions and classes from Python modules

Usage:
  pydefs [<module>]...
  pydefs -h | --help
  pydefs --version

Examples:
  pydefs path/to/my/module.py
    List functions/classes for a single module

  pydefs path/to/my/module.py path/to/another/module.py
    List functions/classes for multiple modules

  pydefs path/to/my/modules
    List functions/classes for all modules in a package

Options:
  -h --help    Show program help
  --version    Show program version
"""

import os
import re

from docopt import docopt

from pydefs.version import __version__


def main():
    """ Entry point for invoking the pydefs module. """

    arguments = docopt(__doc__, version='pydefs ' + __version__)

    paths = arguments['<module>']

    for path in paths:
        pass


if __name__ == '__main__':
    main()
