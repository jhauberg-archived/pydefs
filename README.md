# pydefs

A CLI for listing function and class definitions from Python modules (without importing them).

For example, running `pydefs` against itself:

    $ pydefs pydefs/
    pydefs
    pydefs/__init__.py (0 definitions)
    pydefs/__main__.py (1 definition)
    33: main
    pydefs/parse.py (6 definitions)
    07: defs
    30: parse_ast
    35: parse_path
    42: parse_file
    56: parse_directory
    67: print_definitions
    pydefs/version.py (0 definitions)

# Installation

You can install `pydefs` straight from the source:

    $ python3 setup.py install

# Usage

When installed, you can run `pydefs` on the command line:

    $ pydefs path/to/module.py another/module.py

<details>
  <summary>**Running without installing**</summary>

You can also run `pydefs` without installing it first. However, in that case, you must execute the `pydefs` package as a module.

Assuming your working directory is the root of the `pydefs` project, you go like this:

    $ python3 -m pydefs path/to/module.py
</details>

<details>
  <summary>**Uninstalling**</summary>

If you wish to uninstall `pydefs` and make sure that you get rid of everything, you can run the installation again using the additional **--record** argument to save a list of all installed files:

    $ python3 setup.py install --record installed_files.txt

Then, you can then go through all the listed files and manually delete each one.
</details>

## Requirements

This project strives to be small and specific in focus, as well as keeping dependencies at an absolute minimum.

  * Python 3.5 - type hinting,
  * [docopt](https://github.com/docopt/docopt) - provides a nicer command-line interface

## Full usage

```
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
```

# Contributing

If you find any problems using this software, please [open an issue](https://github.com/jhauberg/pydefs/issues/new) or submit a fix as a pull request.

Please refer to [CONTRIBUTING](CONTRIBUTING.md) for further information.

## License

    Copyright 2016 Jacob Hauberg Hansen.

    Permission is hereby granted, free of charge, to any person obtaining a copy of
    this software and associated documentation files (the "Software"), to deal in
    the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
    of the Software, and to permit persons to whom the Software is furnished to do
    so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    http://en.wikipedia.org/wiki/MIT_License
